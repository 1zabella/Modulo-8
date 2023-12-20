from nbresult import ChallengeResultTestCase

class TestSubmissionBaseline(ChallengeResultTestCase):

    def test_score_baseline(self):
        self.assertLess(self.result.score_baseline, 0.23)

    def test_submission_shape(self):
        self.assertEqual(self.result.submission_shape, (1459,2))
                         
    def test_submission_columns(self):
        self.assertEqual(self.result.submission_columns, ['Id', 'SalePrice'])

    def test_submission_dtypes(self):
        self.assertEqual(self.result.submission_dtypes, "[dtype('int64'), dtype('float64')]")
