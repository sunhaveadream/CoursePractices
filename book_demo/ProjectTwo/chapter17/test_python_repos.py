#try17-3
#2022/11/6
#author:linxu
import unittest
import python_repos as pr

import unittest
import python_repos as pr

class PythonReposTestCase(unittest.TestCase):
    def setUp(self):
     self.r = pr.get_response()
     self.repo_dicts = pr.get_repo_dicts(self.r)
     self.repo_dict = self.repo_dicts[0]
     self.repo_links, self.stars, self.labels = pr.get_project_data(self.repo_dicts)

    def test_get_response(self):
     self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
     self.assertEqual(len(self.repo_dicts), 30)
     required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
     for key in required_keys:
        self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()
