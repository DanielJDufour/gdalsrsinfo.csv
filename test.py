from csv import DictReader
import unittest

class Test(unittest.TestCase):

  def setUp(self):
    with open('gdalsrsinfo.csv', 'r') as f:
      self.rows = list(DictReader(f, delimiter="\t"))

  def test_length(self):
    self.assertGreater(len(self.rows), 1000)

  def test_esriwkt(self):
    uniques = set([row['ESRI WKT'] for row in self.rows])
    self.assertGreater(len(uniques), 1000)

  def test_proj4js(self):
    uniques = set([row['PROJ.4'] for row in self.rows])
    self.assertGreater(len(uniques), 1000)

  def test_wkt(self):
    uniques = set([row['OGC WKT2'] for row in self.rows])
    self.assertGreater(len(uniques), 1000)

if __name__ == '__main__':
    unittest.main()