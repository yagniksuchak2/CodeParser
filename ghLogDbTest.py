import unittest
import ghLogDb


class ghLogDbTest(unittest.TestCase):

    def setUp(self):
        self.testCommit1=ghLogDb.ghLogDb("test_case/TestCommit1.txt")
        self.testCommit1.processLog()
        self.testCommit2=ghLogDb.ghLogDb("test_case/TestCommit2.txt")
        self.testCommit2.processLog()





    def test_Commit1(self):

        shas = self.testCommit1.shas
        self.assertTrue(len(shas) == 1) #Just 1 commit.
        self.assertTrue(shas[0].author == "Kevin Sawicki")
        patches = shas[0].patches
        self.assertTrue(len(patches) == 1)
        for patch in patches:
            self.assertTrue(patch.language == "java")
            self.assertTrue(patch.is_test == False)
            print(patch.file_name)

        self.assertTrue(patches[0].file_name == "app/src/main/java/com/github/mobile/accounts/AccountUtils.java")
        methods = patches[0].methods

        self.assertTrue(len(methods) == 1)
        self.assertTrue(methods[0].method == "getAccounts")
        self.assertTrue(methods[0].total_add == 1)
        self.assertTrue(methods[0].total_del == 2)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,methods[0].exceptionDictonary)





if __name__=="__main__":
    unittest.main()