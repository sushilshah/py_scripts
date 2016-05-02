import requests
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool 

def getSpeed(url, test_time=3) :
  localFilename = url.split('/')[-1]
  start = time.clock()
  r = requests.get(url, stream=True)
  total_length = r.headers.get('content-length')
  dl = 0
  if total_length is None: # no content length header
    print ('total_length %s ' %r.content)
  else:
    for chunk in r.iter_content(1024):
      dl += len(chunk)
      done = int(50 * time.clock() - start / int(test_time))
      sys.stdout.write("\r[%s%s] %s second" % ('=' * done, ' ' * (50-done), dl//(time.clock() - start)))
      if time.clock() - start >= test_time:
        #bps to kbps
        return (dl//(time.clock() - start))/1000000
  
  return (dl//(time.clock() - start))/1000000

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
        done = int(50 * dl / int(total_length))
        sys.stdout.write("\r[%s%s] %s bps" % ('=' * done, ' ' * (50-done), dl//(time.clock() - start)))

  return (time.clock() - start)

def test_servers_speed():
  server_1_eng = 'http://58.65.128.60:803/'
  server_2_eng = 'http://58.65.128.63:803/'
  
  server_3_eng_ag = 'http://58.65.128.51:604/'
  server_3_eng_hr = 'http://58.65.128.51:602/'
  server_3_eng_sz = 'http://58.65.128.51:603/'
  
  server_4_eng_af = 'http://58.65.128.57:614/'
  server_4_eng_gk = 'http://58.65.128.57:616/'
  server_4_eng_lz = 'http://58.65.128.57:615/'
  sample_movie_s1 = 'http://58.65.128.60:803/English%20Movies%20(A%20-%20G)/A%20Beautiful%20Mind/A%20Beautiful%20Mind.avi'
  sample_movie_s2 = 'http://58.65.128.63:803/English%20Movies%20(A%20-%20G)/A%20Beautiful%20Mind/A%20Beautiful%20Mind.avi'
  sample_movie_s3 = 'http://58.65.128.51:604/English%20Movies%20(A%20-%20G)/A%20Beautiful%20Mind/A%20Beautiful%20Mind.avi'
  sample_movie_s4 = 'http://58.65.128.57:614/English%20Movies%20(A%20-%20F)/A%20Beautiful%20Mind/A%20Beautiful%20Mind.avi'

  urls = [sample_movie_s1,sample_movie_s2,sample_movie_s3,sample_movie_s4]

  pool = ThreadPool(4) 

  # Open the urls in their own threads
  # and return the results
  results = pool.map(getSpeed, urls)

  #close the pool and wait for the work to finish 
  pool.close() 
  pool.join() 
  print ("\n Speed Results: ")
  svr = 1
  for i in results:
    sys.stdout.write("\r\n Server %s  speed : %s mbps" % (svr, i))
    svr+=1
  sys.stdout.write("\r\n ----------------------------------------- Speed Test Completed ------------------------------------ \r\n" )

def main() :
  if len(sys.argv) > 1 :
        url = sys.argv[1]
  else :
        #url = raw_input("Enter the URL : ")
        url = 'http://58.65.128.60:803/English%20Movies%20(A%20-%20G)/Eddie%20The%20Eagle%202016%20720p/Eddie%20The%20Eagle%202016%20720p.mkv'
        #directory = raw_input("Where would you want to save the file ?")
        directory = "d:/"

        #test speed of servers and fix a server from where to download
        #ask for movie name
        #get movie and write it to the directory
        #show progress
  test_servers_speed()
  #time_elapsed = downloadFile(url, directory)
  #print "Download complete..."
  #print "Time Elapsed: " + str(time_elapsed)


if __name__ == "__main__" :
  main()