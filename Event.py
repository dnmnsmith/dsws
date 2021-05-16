from datetime import datetime


class Event:

    def __init__(self, location, desc, value, time=None) -> None:
        if time is None:
            self._time = datetime.now()
        elif isinstance(time,str):
            if time[10]!=' ':
                self._time=datetime.fromisoformat(time[0:10] + " " + time[10:])
            else:
                self._time=datetime.fromisoformat(time)
        elif isinstance(time,datetime):
            self._time = time
        else:
            raise RuntimeError(f"Unable to handle datetime {time}")

        self._location = location
        self._desc = desc
        self._value = float(value)

    def location( self, location = None):
        if not location is None:
            self._location = location
        return self._location

    def time( self, time = None):
        if not time is None:
            self._time = time
        return self._time

    def timestamp(self):
        return str(self.time()).replace(' ','')

    def desc( self, desc = None):
        if not desc is None:
            self._desc = desc
        return self._desc

    def value( self, value = None):
        if not value is None:
            self._value = float(value)
        return self._value
    
    def __str__(self):
        return "Loc={} Time={} Desc={} Value={}".format(self._location,self._time,self._desc,self._value)

    def __eq__(self, other): 
        if not isinstance(other, Event):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self._location == other._location and self._time == other._time and self._desc == other._desc and self._value == other._value

    def makeKey( location,description):
        return (location,description)

    def getKey(self):
        return Event.makeKey( self._location, self._desc )
    
    def copy(self):
        return Event(self.location(),self.desc(),self.value(),self.time())
