import sys
sys.path.insert(0, '.')
from Webpage import *

hello = Webpage("bob")
brewTimes = [.1,.3,.5,.2]

res = hello.startBrewing(brewTimes)
print(res)
