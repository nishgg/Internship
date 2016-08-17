import logging
import datetime
import os
import os.path
import glob

def formatName(filename, date=None):
    if date is None:
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day)

    else:
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)

    strdate = "%s-%s-%s-%s.log" % (filename, year, month, day)

    return strdate

def checkRotate(current, path, backupcount):
    if backupcount == 0:
        return False
    else:
        file_path = os.path.join(path, current)
        if os.path.isfile(file_path):
            return False
        else:
            return True


def rotate(filename, path, backupCount):
    files = glob.glob(filename + "*.log")

    for num in range(backupCount):
        if len(files) == 0:
            return

        files.remove(max(files))

    for file in files:
        del_path = os.path.join(path, file)
        os.unlink(del_path)

    return


def getLogger(log_name="machine-learning-python", filename="ML_python", log_level=logging.WARN, backupCount=1, path=None):

  if path is None:
      path = os.getcwd()

  fname = formatName(filename)
  if checkRotate(fname, path, backupCount):
      rotate(filename, path, backupCount)

  log = logging.getLogger(log_name)
  log.setLevel(log_level)
  formatter = logging.Formatter('%(asctime)s - %(levelname)s in %(filename)s - %(funcName)s: %(message)s')
  handler = logging.FileHandler(filename=fname)
  handler.setFormatter(formatter)
  log.addHandler(handler)

  return log

if __name__ == "__main__":
    l = getLogger()
    l.warn("test")