
def toStr(text):
  try:
    text1 = str(text).encode('iso-8859-1')
    temp_text = text1.replace("\'","\"")
    temp_text = temp_text.strip()
    return "\'" + str(temp_text) + "\'"
  except:
    print type(text)
    return "\'NA\'"


class PatchMethod:

  def __init__(self, methodName):

    self.method  = methodName

    self.exception_add = 0 # No. of assertion added
    self.exception_del = 0 # No. of assertion deleted
    self.total_add  = 0 # No. of lines added
    self.total_del  = 0 # No. of lines deleted
    self.exceptionDictonary={}

  def printPatch(self):

    #retStr  = "\n\t\t------ Method -----\n"
    retStr  = ""
    retStr += "\t\tmethod      = %s\n" % (self.method)
    #retStr += "\t\texception_add  = %d\n" % (self.exception_add)
    #retStr += "\t\texception_del  = %d\n" % (self.exception_del)
    retStr += "\t\ttotal_add   = %d\n" % (self.total_add)
    retStr += "\t\ttotal_del   = %d\n" % (self.total_del)
    retStr += "\t\texcepDict   = %s\n" % (self.exceptionDictonary)
    retStr += "\t\texception_add   = %s\n" % (self.exception_add)
    retStr += "\t\texception_del   = %s\n" % (self.exception_del)



    return retStr

  def dumpMethod(self):

    method      = toStr(self.method)
    exception_add  = toStr(self.exception_add)
    exception_del  = toStr(self.exception_del)
    total_add   = toStr(self.total_add)
    total_del   = toStr(self.total_del)

    methodStr = (",").join((method,exception_add,exception_del,total_add,total_del))
    return methodStr


  def dictToCsv(self):
      dictStr=""
      for key, value in self.exceptionDictonary.iteritems():
          if dictStr=="":
            dictStr= dictStr+str(value)
          else:
            dictStr= dictStr+","+str(value)
          # if dictStr=="":
          #   dictStr= dictStr+(",").join((str(value)))
          # else:
          #   dictStr= dictStr+","+(",").join((str(value)))



      return str(dictStr)

  def methodToCsv(self):

    method      = toStr(self.method).replace(","," ")
    total_add   = toStr(self.total_add)
    total_del   = toStr(self.total_del)
    unique_exception_add=toStr(self.exception_add)
    unique_exception_del=toStr(self.exception_del)

    methodStr = (",").join((method,total_add,total_del,unique_exception_add,unique_exception_del,self.dictToCsv()))
    return methodStr


