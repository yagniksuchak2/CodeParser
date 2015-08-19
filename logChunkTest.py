import unittest
import logChunk

class logChunktest(unittest.TestCase):

    def readHelper(self,filename):
        inf =open(filename,"r")
        text=""
        for line in inf:
            text+=line

        return text

    def setUp(self):

        self.testChunk = logChunk.logChunk("")
        #Read in the full tests
        self.chunk1 = logChunk.logChunk(self.readHelper("testChunk1.txt"))
        self.chunk2 = logChunk.logChunk(self.readHelper("testChunk2.txt"))
        self.chunk3 = logChunk.logChunk(self.readHelper("testChunk3.txt"))
        self.chunk4 = logChunk.logChunk(self.readHelper("testChunk4.txt"))
        self.chunk5 = logChunk.logChunk(self.readHelper("testChunk5.txt"))
        self.chunk6 = logChunk.logChunk(self.readHelper("testChunk6.txt"))
        self.chunk7 = logChunk.logChunk(self.readHelper("testChunk7.txt"))
        self.chunk8 = logChunk.logChunk(self.readHelper("testChunk8.txt"))
        self.chunk9 = logChunk.logChunk(self.readHelper("testChunk9.txt"))







    def test_parseText(self):

        self.chunk1.parseText()
        self.chunk2.parseText()
        self.chunk3.parseText()
        self.chunk4.parseText()
        self.chunk5.parseText()
        self.chunk6.parseText()
        self.chunk7.parseText()
        self.chunk8.parseText()
        self.chunk9.parseText()


#parsing done

#check chunk1

        funcList = self.chunk1.functions
        self.assertTrue(len(funcList) == 2) #Should be no mock function for asserts
        self.assertTrue(self.chunk1.isExceptionChunkFlag==True)
        self.assertTrue(self.chunk1.bracketMisMatch==0)

        self.assertTrue(funcList[0].name=="foo")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 1)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 2)
        self.assertTrue(temp.total_del == 1)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 1, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 1, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==1)
        self.assertTrue(temp.exception_del==1)


        self.assertTrue(funcList[1].name=="foo00022")
        self.assertTrue(funcList[1].total_add == 4)
        self.assertTrue(funcList[1].total_del == 2)
        self.assertTrue(self.chunk1.isExceptionChunkFlag==True)
        temp = funcList[1].convertToPatchMethod()
        self.assertTrue(temp.total_add == 4)
        self.assertTrue(temp.total_del == 2)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 1, 'try Dels': 1, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 1, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[1].excepDict)

        self.assertTrue(temp.exception_add==2)
        self.assertTrue(temp.exception_del==1)


#check chunk2

        funcList = self.chunk2.functions
        self.assertTrue(len(funcList) == 2) #Should be no mock function for asserts
        self.assertTrue(self.chunk2.isExceptionChunkFlag==True)
        self.assertTrue(self.chunk2.bracketMisMatch==0)

        self.assertTrue(funcList[0].name=="getAccounts")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 2)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 1)
        self.assertTrue(temp.total_del == 2)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)

        self.assertTrue(funcList[1].name=="getAccount")
        self.assertTrue(funcList[1].total_add == 6)
        self.assertTrue(funcList[1].total_del == 2)
        self.assertTrue(self.chunk1.isExceptionChunkFlag==True)
        temp = funcList[1].convertToPatchMethod()
        self.assertTrue(temp.total_add == 6)
        self.assertTrue(temp.total_del == 2)
        dict= {'throw Adds':1, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 2, 'try Dels': 2, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 4, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertTrue(temp.exception_add==6)
        self.assertTrue(temp.exception_del==2)


        self.assertEqual(dict,funcList[1].excepDict)

#check chunk3

        funcList = self.chunk3.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk3.isExceptionChunkFlag==True)
        self.assertTrue(self.chunk3.bracketMisMatch==0)

        self.assertTrue(funcList[0].name=="ReflectiveProperty")
        self.assertTrue(funcList[0].total_add == 12)
        self.assertTrue(funcList[0].total_del == 3)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 12)
        self.assertTrue(temp.total_del == 3)
        dict= {'throw Adds':0, 'catch Dels': 1, 'throw Dels': 0, 'try Adds': 8, 'try Dels': 2, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 4, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==12)
        self.assertTrue(temp.exception_del==3)


#check chunk4

        funcList = self.chunk4.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk4.isExceptionChunkFlag==0)
        self.assertTrue(self.chunk4.bracketMisMatch==0)

        self.assertTrue(funcList[0].name=="setHandle")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 1)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 1)
        self.assertTrue(temp.total_del == 1)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==0)
        self.assertTrue(temp.exception_del==0)


#check chunk5

        funcList = self.chunk5.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk5.isExceptionChunkFlag==0)
        self.assertTrue(self.chunk5.bracketMisMatch==0)

        self.assertTrue(funcList[0].name=="copy")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 5)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 1)
        self.assertTrue(temp.total_del == 5)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==0)
        self.assertTrue(temp.exception_del==0)


#check chunk6

        funcList = self.chunk6.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk5.isExceptionChunkFlag==0)
        self.assertTrue(self.chunk5.bracketMisMatch==0)

        self.assertTrue(funcList[0].name=="init")
        self.assertTrue(funcList[0].total_add == 0)
        self.assertTrue(funcList[0].total_del == 1)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 0)
        self.assertTrue(temp.total_del == 1)
        dict= {'throw Adds':0, 'catch Dels': 1, 'throw Dels': 1, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==0)
        self.assertTrue(temp.exception_del==1)

#check chunk7

        funcList = self.chunk7.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk7.isExceptionChunkFlag==1)
        self.assertTrue(self.chunk7.bracketMisMatch==0)


        self.assertTrue(funcList[0].name=="loadData")
        self.assertTrue(funcList[0].total_add == 1)
        self.assertTrue(funcList[0].total_del == 4)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 1)
        self.assertTrue(temp.total_del == 4)
        dict= {'throw Adds':0, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds': 0, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==0)
        self.assertTrue(temp.exception_del==0)

#check chunk8

        funcList = self.chunk8.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk8.isExceptionChunkFlag==1)
        self.assertTrue(self.chunk8.bracketMisMatch==0)


        self.assertTrue(funcList[0].name=="getAuthToken")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 2)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 2)
        self.assertTrue(temp.total_del == 2)
        dict= {'throw Adds':1, 'catch Dels': 1, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds':2, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==2)
        self.assertTrue(temp.exception_del==1)

#check chunk9

        funcList = self.chunk9.functions


        self.assertTrue(len(funcList) == 1) #Should be no mock function for asserts
        self.assertTrue(self.chunk9.isExceptionChunkFlag==1)
        self.assertTrue(self.chunk9.bracketMisMatch==0)


        self.assertTrue(funcList[0].name=="getAuthToken")
        self.assertTrue(funcList[0].total_add == 2)
        self.assertTrue(funcList[0].total_del == 2)
        temp = funcList[0].convertToPatchMethod()
        self.assertTrue(temp.total_add == 2)
        self.assertTrue(temp.total_del == 2)
        dict= {'throw Adds':1, 'catch Dels': 0, 'throw Dels': 0, 'try Adds': 0, 'try Dels': 0, 'exception Dels': 0, 'raise Adds': 0, 'catch Adds':2, 'finally Dels': 0, 'finally Adds': 0, 'exception Adds': 0, 'raise Dels': 0}
        self.assertEqual(dict,funcList[0].excepDict)
        self.assertTrue(temp.exception_add==2)
        self.assertTrue(temp.exception_del==0)


if __name__=="__main__":
    unittest.main()