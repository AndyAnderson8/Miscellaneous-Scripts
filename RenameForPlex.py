import os
import shutil

ogDirectory = input("Enter folder path: ")
os.makedirs(ogDirectory + "/temp")

def moveVideos(directory):
  for file in os.listdir(directory):
    fileDir = os.path.join(directory, file)
    if os.path.isdir(fileDir):
      if file != "temp":
        moveVideos(fileDir)
    else:
      fileType = file.rsplit(".", 1)[1].lower()
      if fileType == "mp4" or fileType == "mkv" or fileType == "mov" or fileType == "avi" or fileType == "avchd" or fileType == "flv" or fileType == "f4v" or fileType == "swf" or fileType == "webm":
        os.rename(fileDir, ogDirectory + "/temp/" + file)

def deleteOtherFiles(directory):
  for file in os.listdir(directory):
    if file != "temp":
      fileDir = os.path.join(directory, file)
      if os.path.isdir(fileDir):
        deleteOtherFiles(fileDir)
        os.rmdir(fileDir)
      else:
        os.remove(fileDir)

def renameMovies(directory):
  for file in os.listdir(directory):
    fileDir = os.path.join(directory, file)
    fileType = file.rsplit(".", 1)[1]
    fileName = file.rsplit(".", 1)[0].replace("x264", "").replace("AAC", "").replace("RARBG", "").replace("EAC3", "").replace("10bit", "").replace("HEVC", "").replace("BluRay", "").replace("WEBRip", " ").replace("1080p", "").replace("720p", "").replace("YTS.AM", "").replace("AMZN", "").replace("x265", "").replace("5.1", "").replace("NF", "").replace("WEB-DL", "").replace("YTS.MX", "").replace("[", "").replace("YTS.AG", "").replace("YTS.LT", "").replace("WEB", "").replace(".", " ").replace("[", "").replace("]", "").replace("-", "").replace("(", "").replace(")", "")
    substrings = fileName.split(" ")
    i = 0
    for substring in substrings:
      if substring.isalpha():
        fileName = fileName.replace(substring, substring.capitalize())
      elif len(substring) == 4 and ((substring[0] == "1" and substring[1] == "9") or substring[0] == "2"):
        if i != 0:
          fileName = fileName.split(substring)[0] + "(" + substring + ")"
        else:
          fileName = fileName.replace(substring, "") + "(" + substring + ")"
        break
      i += 1
    os.rename(fileDir, directory + "/" + fileName + "." + fileType)

def cleanUp(directory):
  for file in os.listdir(directory + "/temp"):
    os.rename(directory + "/temp/" + file, directory + "/" + file)
  os.rmdir(directory + "/temp")

def moveFiles(startDir, endDir):
  for file in os.listdir(startDir):
    fileDir = os.path.join(startDir, file)
    shutil.move(fileDir, endDir + "/" + file)

moveVideos(ogDirectory)
deleteOtherFiles(ogDirectory)
renameMovies(ogDirectory + "/temp")
cleanUp(ogDirectory)
#waiting = input("Press enter to move files: ")
#moveFiles(ogDirectory, "P:/Movies")