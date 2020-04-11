# https://trinket.io/python/63c3917709?outputOnly=true

# Start classes with Capital
class Room():

  # constructor method tells Python how to create a class
  def __init__(self, room_name):
    self.name = room_name
    self.description = None #TODO

    # we create setters and getters to get data from the objects we create
# create a setter that sets the data
  def set_description(self, room_description):
    self.description = room_description

  # create a getter that gets the data
  def get_description(self):
    return self.description

  # Add a getter method called get_name and a setter method called set_name to your class to allow someone to get and set the attribute name in the same way.
  def set_name(self, room_name):
    self.name = room_name

  def get_name(self):
    return self.name

  def describe(self):
    print(self.description)
