from abc import ABCMeta, abstractmethod
from datetime import datetime

class reservation(object):
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

class Deal(object):
  __metaclass__ = ABCMeta

  def __init__(self, rate, txt, dealValue, dealtype, startDate, endDate):
#    self._hotel_name = hotel_name
    self._nightlyRate = rate
    self._promoTxt = txt
    self._dealValue = dealValue
    self._dealType = dealtype
    print startDate, endDate
    self._startDate = datetime.strptime(startDate, "%Y-%m-%d").date()
    self._endDate = datetime.strptime(endDate, "%Y-%m-%d").date()

  # @staticmethod
  # def getDealType():
  #   DealType = ['REBATE', 'REBATE_3PLUS', 'PCT']
  #   return DealType

  # def getHotelName(self):
  #   return self._hotel_name

  def getValue(self):
    return self._dealValue

  def getPromoTxt(self):
    return self._promoTxt

  @abstractmethod
  def isApplicable(self, rsv):
    pass


  @abstractmethod
  def getDiscount(self, rsv):
    pass

  def isDateWithin(self, givendate):
    return ((givendate > self._startDate) and (givendate < self._endDate))

  def factory(dealtype):
    if dealtype == "rebate":
      return DealRebate(rate, txt, dealValue, dealtype, startDate, endDate)
    elif dealtype == "rebate_3plus":
      return DealRebate3Plus(rate, txt, dealValue, dealtype, startDate, endDate)
    elif dealtype == "pct":
      return DealPct(rate, txt, dealValue, dealtype, startDate, endDate)
  # factory = staticmethod(factory)

class DealPct(Deal):

  def __init__(rate, txt, dealValue, dealtype, startDate, endDate):
    super(Deal, self).__init__(rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    return (rsv.getCheckin() > self._startDate) and (rsv.getCheckin() < self._endDate)

  def getDiscount(self, rsv):
    return (self._dealValue/100)* self._nightlyRate * rsv.getNights()

class DealRebate(Deal):

  # def DealRebate(hotel, rate, txt, dealValue, dealtype, startDate, endDate):
  #   super(hotel, rate, txt, dealValue, dealtype, startDate, endDate)
  def __init__(rate, txt, dealValue, dealtype, startDate, endDate):
    super(Deal, self).__init__(rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    return (rsv.getCheckin() > self._startDate) and (rsv.getCheckin() < self._endDate)

  def getDiscount(self, rsv):
    return (self._dealValue/100)* self._nightlyRate * rsv.getNights()

class DealRebate3Plus(Deal):

  # def DealRebate3Plus(hotel, rate, txt, dealValue, dealtype, startDate, endDate):
  #   super(hotel, rate, txt, dealValue, dealtype, startDate, endDate)
  def __init__(rate, txt, dealValue, dealtype, startDate, endDate):
    super(Deal, self).__init__(rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    return (rsv.getCheckin() > self._startDate) and (rsv.getCheckin() < self._endDate)

  def getDiscount(self, rsv):
    return (self._dealValue/100)* self._nightlyRate * rsv.getNights()

