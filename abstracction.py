import abc 
from abc import *
class mnc(ABC):
    @abstractmethod
    def origin(self):
        pass
class tcs(mnc):
    def origin(self):
        print("TCS has been established in 1968 in India.")
class google(mnc):
    def origin(self):
        print("Google has been established in 1998 in United States.")
class siemens(mnc):
    def origin(self):
        print("Siemens has been established in 1847 in Germany.")
class Marolix(mnc):
    def origin(self):
        print("Marolix has been established in 2011 in India.")
t=tcs()
t.origin()
g=google()
g.origin()
m=Marolix()
m.origin()
s=siemens()
s.origin()
for i in (t,g,m,s):
    i.origin()