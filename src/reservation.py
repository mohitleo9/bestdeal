from datetime import date

class Reservation(object):
  def __init__(self, hotel, checkinDate, nights):
    self.hotel = hotel;
    self.checkin = checkinDate;
    self.nights = nights;

  def getCheckin(self):
    return self.checkin

  def getHotel(self):
    return self.hotel

  def getNights(self):
    return self.nights

