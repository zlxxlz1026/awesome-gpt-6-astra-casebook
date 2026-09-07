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
            with patch.object(catalog,'ROOT',root), patch('sys.argv',['catalog.py','add-source','https://twitter.com/changed/status/2096460180401889613?s=20','--reason','duplicate']):
                with patch('builtins.print'): catalog.main()
            self.assertEqual(path.read_text(), content)

if __name__=='__main__': unittest.main()
