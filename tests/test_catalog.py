import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('catalog',Path(__file__).resolve().parents[1]/'scripts/catalog.py')
catalog=importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

class CatalogTests(unittest.TestCase):
    def test_aliases_have_same_id(self):
        for url in ['https://x.com/user/status/2096460180401889613?s=20', 'https://twitter.com/renamed/status/2096460180401889613/photo/1#x', 'https://mobile.twitter.com/user/status/2096460180401889613/video/2', 'https://x.com/i/web/status/2096460180401889613']:
            self.assertEqual(catalog.normalize_url(url)[0], '2096460180401889613')

    def test_reject_non_posts_and_spoofed_hosts(self):
        for url in ['https://x.com/user', 'https://x.com.evil.com/u/status/12', 'https://t.co/abc', 'https://x.com/u/status/12/analytics', 'https://evil@x.com/u/status/12', 'ftp://x.com/u/status/12']:
            with self.assertRaises(ValueError): catalog.normalize_url(url)

    def test_seed_catalog_valid(self):
        catalog.validate()

    def test_editorial_sources_cannot_reference_another_case(self):
        original = catalog.read
        def read(name):
            rows = original(name)
            if name == 'case-notes.json':
                rows[0]['source_ids'] = ['2096069303523033434']
            return rows
        with patch.object(catalog, 'read', read):
            with self.assertRaises(AssertionError):
                catalog.validate()

    def test_editorial_notes_preserve_and_follow_original_prompt(self):
        files = catalog.render()
        cases = {c['id']: c for c in catalog.read('cases.json')}
        for note in catalog.read('case-notes.json'):
            c = cases[note['case_id']]
            for suffix, heading in [('', '#### Prompt breakdown — editorial analysis'), ('.zh-CN', '#### 提示词拆解 · 项目分析')]:
                for path in [f'docs/categories/{c["category"]}{suffix}.md', f'docs/gallery{suffix}.md']:
                    section = files[path].split(f'<a id="{c["id"]}"></a>', 1)[1].split('<a id=', 1)[0]
                    self.assertIn(c['prompt']['text'], section)
                    self.assertGreater(section.index(heading), section.index(c['prompt']['text']))

    def test_editorial_copy_avoids_untested_status_disclaimers(self):
        root = Path(__file__).resolve().parents[1]
        paths = [root / 'scripts/catalog.py', root / 'data/case-notes.json',
                 root / 'docs/reproduction/README.md', *sorted((root / 'docs/guides').glob('*.md'))]
        banned = [
            'Suggested checks, not executed', '建议验收，尚未执行',
            'have not been tested', '尚未实测', '待验证模板',
            'does not claim every example has been independently reproduced',
            '不声称所有案例均经过独立复现',
            'does not guarantee reproduction', '不保证复现效果',
            'No independent reproduction report has been completed',
            '本轮尚未完成独立复现报告', '记录“未测”',
        ]
        for path in paths:
            content = path.read_text(encoding='utf-8')
            for phrase in banned:
                with self.subTest(path=path.relative_to(root), phrase=phrase):
                    self.assertNotIn(phrase, content)

    def test_english_editorial_labels_use_english_colons(self):
        files = catalog.render()
        labels = ('Goal', 'Constraints', 'Deliverable', 'Suggested checks', 'Takeaway')
        for path, content in files.items():
            if path == 'docs/gallery.md' or (path.startswith('docs/categories/') and '.zh-CN.' not in path):
                for label in labels:
                    self.assertNotIn(f'**{label}**：', content)

    def test_category_pages_partition_cases_and_preserve_gallery_anchors(self):
        files = catalog.render()
        cases = catalog.read('cases.json')
        active = {c['category'] for c in cases}
        for suffix, lang in [('', 'en'), ('.zh-CN', 'zh')]:
            pages = {category: files[f'docs/categories/{category}{suffix}.md'] for category in active}
            for c in cases:
                anchor = f'<a id="{c["id"]}"></a>'
                self.assertIn(anchor, files[f'docs/gallery{suffix}.md'])
                self.assertIn(anchor, pages[c['category']])
                self.assertEqual(sum(anchor in page for page in pages.values()), 1)
                status = ('Full prompt' if lang == 'en' else '完整提示词') if c['prompt']['display'] == 'full' else ('Prompt excerpt' if lang == 'en' else '提示词摘录')
                detail = pages[c['category']].split(anchor, 1)[1].split('<a id=', 1)[0]
                self.assertIn(f'**{status}**', detail)

    def test_cover_selection_survives_case_reordering(self):
        import re
        original = catalog.read
        before = catalog.render()['README.md']
        def read(name):
            rows = original(name)
            return list(reversed(rows)) if name == 'cases.json' else rows
        with patch.object(catalog, 'read', read):
            after = catalog.render()['README.md']
        self.assertEqual(re.findall(r'<img [^>]+>', before), re.findall(r'<img [^>]+>', after))

    def test_reject_cover_from_another_category(self):
        original = catalog.read
        def read(name):
            rows = original(name)
            if name == 'categories.json':
                rows[0]['cover']['case_id'] = 'astral-liquid-glass'
            return rows
        with patch.object(catalog, 'read', read):
            with self.assertRaises(AssertionError):
                catalog.validate()

    def test_catalog_keeps_the_initial_thirty_case_milestone(self):
        self.assertGreaterEqual(len(catalog.read('cases.json')), 30)

    def test_every_case_has_a_public_prompt_and_no_reproduction_status(self):
        for case in catalog.read('cases.json'):
            self.assertEqual(case['prompt']['availability'], 'public')
            self.assertNotIn('reproduction', case)

    def test_release_sources_all_support_curated_cases(self):
        for source in catalog.read('sources.json'):
            self.assertEqual(source['status'], 'accepted')
            self.assertIsNotNone(source['case_id'])

    def test_collection_index_lists_every_case_and_source(self):
        files=catalog.render()
        index=files['docs/collection-index.md']
        for case in catalog.read('cases.json'):
            self.assertIn(f'`{case["id"]}`', index)
            for source_id in case['source_ids']:
                self.assertIn(f'[{source_id}]', index)

    def test_reject_duplicate_source(self):
        original=catalog.read
        def read(name):
            rows=original(name)
            return rows+[rows[0]] if name=='sources.json' else rows
        with patch.object(catalog,'read',read):
            with self.assertRaises(AssertionError): catalog.validate()

    def test_reject_missing_translation(self):
        original=catalog.read
        def read(name):
            rows=original(name)
            if name=='cases.json': rows[0]['summary']['zh']=''
            return rows
        with patch.object(catalog,'read',read):
            with self.assertRaises(AssertionError): catalog.validate()

    def test_duplicate_registration_does_not_write(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'data').mkdir()
            path=root/'data/sources.json'
            content=json.dumps(catalog.read('sources.json'))
            path.write_text(content)
            with patch.object(catalog,'ROOT',root), patch('sys.argv',['catalog.py','add-source','https://twitter.com/changed/status/2096147245775331419?s=20','--reason','duplicate']):
                with patch('builtins.print'): catalog.main()
            self.assertEqual(path.read_text(), content)

if __name__=='__main__': unittest.main()
