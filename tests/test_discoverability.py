import importlib.util
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('github_repo', ROOT / 'scripts/github_repo.py')
github_repo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(github_repo)


class DiscoverabilityTests(unittest.TestCase):
    def test_documentation_links_resolve(self):
        # Verify reader navigation across hand-written guides and generated galleries.
        pages = list(ROOT.glob('*.md')) + list((ROOT / 'docs').rglob('*.md'))
        for page in pages:
            content = re.sub(r'```.*?```', '', page.read_text(encoding='utf-8'), flags=re.S)
            for match in re.finditer(r'\]\(([^)]+)\)|href="([^"]+)"', content):
                url = urlsplit(match.group(1) or match.group(2))
                if url.scheme or url.netloc:
                    continue
                target = (page.parent / unquote(url.path)).resolve() if url.path else page
                with self.subTest(page=page.relative_to(ROOT), link=url.geturl()):
                    self.assertTrue(target.is_file(), f'Missing link target: {target}')
                    if url.fragment and target.name.startswith('gallery'):
                        self.assertIn(f'<a id="{url.fragment}"></a>', target.read_text(encoding='utf-8'))

    def test_metadata_merge_preserves_existing_topics_and_is_idempotent(self):
        existing = ['community-examples', 'ai-prompts']
        merged = github_repo.merge_topics(existing)
        self.assertTrue(set(existing).issubset(merged))
        self.assertEqual(merged, github_repo.merge_topics(merged))
        self.assertEqual(len(merged), len(set(merged)))

    def test_topic_overflow_fails_before_any_api_changes(self):
        with self.assertRaises(ValueError):
            github_repo.merge_topics([f'existing-{i}' for i in range(20)])


if __name__ == '__main__':
    unittest.main()
