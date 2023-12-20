from nbresult import ChallengeResultTestCase

class TestFeaturesOverview(ChallengeResultTestCase):

    def test_feat_categorical_small(self):
        self.assertEqual(self.result.n, 34)

