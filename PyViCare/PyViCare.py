from PyViCare.PyViCareGazBoiler import GazBoiler

def handleKeyError(func):
    def wrapper():
        try:
            return func()
        except KeyError as err:
        	return "KeyError: " + str(err)
        except IndexError as err:
            return "IndexError: " + str(err)
    return wrapper

# DEPRECATED
class ViCareSession(GazBoiler):
    def dummy(self):
        print("done")
        