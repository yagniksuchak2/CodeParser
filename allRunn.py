
#get the path of directory in which project directories are there. Assume dirsPath

#rootdir ='C:\Users\Yagnik\PycharmProjects\Top_Project'

import os
import sys
import ghProc
from logChunk import getExceptionKeyword


#print os.listdir(rootdir)
# for subdir, dirs, files in os.walk(rootdir):
#     print dirs


def main():
  print "Utility to BULK process github logs"

  if len(sys.argv) < 2:
  	print "!!! Usage: python allRun.py top_project directory"
  	sys.exit()
  if not os.path.isdir("../Results"):
            os.mkdir("../Results")

  fPtrChangeSummary=open("../Results/"+"ChangeSummary.csv",'w')
  fPtrChangeSummary.write("project,sha,author,commit_date,is_bug\n")
  fPtrPatchSummary=open("../Results/"+"PatchSummary.csv",'w')
  fPtrMisMatchSummary=open("../Results/"+"MisMatchSummary.csv",'w')
  fPtrMisMatchSummary.write("project,Total,Match,MisMatch,Exception,matchException,misMatchException\n")
  lst=[]
  listToDict={}
  getExceptionKeyword(lst)
  for keyword in lst:
      listToDict[str(keyword)+" Adds"]=0
      listToDict[str(keyword)+" Dels"]=0
  fPtrPatchSummary.write("project, sha, language, file_name, is_test,bracket_diff,isExceptionPatch, method_name,total_add,total_del,uniqueExcepAdd,uniqueExcepDel,%s\n"%",".join(listToDict.keys()))

  fPtrChangeSummary.close()
  fPtrPatchSummary.close()
  fPtrMisMatchSummary.close()





  rootdir = sys.argv[1]

  for dir in os.listdir(rootdir):
    path= os.path.join(rootdir,dir)
    print path
    os.system('python ghProc.py %s'%path)

if __name__ == '__main__':
  main()
