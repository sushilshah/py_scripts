# import urllib2 
# from multiprocessing.dummy import Pool as ThreadPool 

# urls = [
#   'http://www.python.org', 
#   'http://www.python.org/about/',
#   'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
#   'http://www.python.org/doc/',
#   'http://www.python.org/download/',
#   'http://www.python.org/getit/',
#   'http://www.python.org/community/',
#   'https://wiki.python.org/moin/',
#   ]

# def makeme(url):
#   print ("make me urls : %s" %url)
#   return "Good"
# # Make the Pool of workers
# pool = ThreadPool(4) 

# # Open the urls in their own threads
# # and return the results
# results = pool.map(makeme, urls)

# #close the pool and wait for the work to finish 
# pool.close() 
# pool.join() 
# print results
# print pool

import sys
sys.stdout.write(str(99) + '\n')
sys.stdout.write('\n' + str(99) + '\n')
