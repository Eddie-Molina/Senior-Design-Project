
import sys
from os.path import dirname
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
import Webpage

#Create the server instance with multithreading capabilities
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
  pass

class Handler(SimpleHTTPRequestHandler):

  #Return HTML File when asked for a get request
  def do_GET(self):
    try:
      d = dirname(dirname(abs(__file__)))
      d = str(d) + '/src/BrewCrew.html'
      f = open(d,'rb')
      #Send the HTML file
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      self.wfile.write(f.read())
      f.close()
      return

    except IOError:
      self.send_error(404,'File Not Found: %s' % self.path)

  #Handle POST Data when given a post request
  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)

    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write('<html><body><h1>POST Test</h1></body></html>')

    print(post_data)

  #Define headers
  def do_HEAD(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

###############################
#            Main             #
###############################

if __name__ == '__main__':
  #This gets the correct port from the command line if used. Default is 192.168.1.254:8080
  if len(sys.argv) == 3:
      PORT = int(sys.argv[2])
      HOST = sys.argv[1]
  else:
      HOST = '192.168.1.254'
      PORT = 8080

  website = Webpage()
  #The server will start up and accept multiple requests
  server = ThreadingSimpleServer((HOST, PORT), Handler)
  #Server will run forever
  server.serve_forever()