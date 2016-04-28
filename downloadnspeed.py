import requests
import sys
import time

def downloadFile(url, directory) :
  localFilename = url.split('/')[-1]
  with open(directory + '/' + localFilename, 'wb') as f:
    start = time.clock()
    r = requests.get(url, stream=True)
    total_length = r.headers.get('content-length')
    dl = 0
    if total_length is None: # no content length header
      f.write(r.content)
    else:
      for chunk in r.iter_content(1024):
        dl += len(chunk)
        f.write(chunk)
        print "TYPES:"
        print type(int(total_length))
        print type(dl)
        done = int(50 * dl / int(total_length))
        sys.stdout.write("\r[%s%s] %s bps" % ('=' * done, ' ' * (50-done), dl//(time.clock() - start)))
        print ''
  return (time.clock() - start)

def main() :
  if len(sys.argv) > 1 :
        url = sys.argv[1]
  else :
        #url = raw_input("Enter the URL : ")
        url = 'http://58.65.128.60:803/English%20Movies%20(A%20-%20G)/Eddie%20The%20Eagle%202016%20720p/Eddie%20The%20Eagle%202016%20720p.mkv'
        #directory = raw_input("Where would you want to save the file ?")
        directory = "d:/"

  time_elapsed = downloadFile(url, directory)
  print "Download complete..."
  print "Time Elapsed: " + time_elapsed


if __name__ == "__main__" :
  main()