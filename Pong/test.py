import unittest
import line
import color

class TestLine(unittest.TestCase):

    def setUp(self):
        self.start, self.end = (0,0)
        self.interval_length = 10
        self.dashed_line = line.Line(self.start, self.end, color.white, 10, line.LineType.DASHED, self.interval_length)

    def test_interval_and_total_dist_no_line(self):
        (dist_interval_x, dist_interval_y, dist_total) = self.dashed_line.interval_and_total_dist(0,0)
        self.assertEqual((dist_interval_x, dist_interval_y, dist_total), (0,0,0))


    def test_interval_and_total_dist_vertical_line(self):
        (dist_interval_x, dist_interval_y, dist_total) = self.dashed_line.interval_and_total_dist(0,20)
        self.assertEqual((dist_interval_x, dist_interval_y, dist_total), (0,10,20))

    def test_interval_and_total_dist_horizontal_line(self):
        (dist_interval_x, dist_interval_y, dist_total) = self.dashed_line.interval_and_total_dist(20,0)
        self.assertEqual((dist_interval_x, dist_interval_y, dist_total), (10,0,20))

    def test_interval_and_total_dist_diagonal_line(self):
        (dist_interval_x, dist_interval_y, dist_total) = self.dashed_line.interval_and_total_dist(20,20)
        self.assertAlmostEqual(dist_interval_x, 10*(1/(2**0.5)))
        self.assertAlmostEqual(dist_interval_y, 10*(1/(2**0.5)))
        self.assertAlmostEqual(dist_total, (20**2+20**2)**0.5)



if __name__ == '__main__':
    unittest.main()

