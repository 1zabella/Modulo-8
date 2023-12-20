from nbresult import ChallengeResultTestCase

class TestPreprocBaseline(ChallengeResultTestCase):

    def test_shape(self):
        self.assertEqual(self.result.shape, (1460,182))

