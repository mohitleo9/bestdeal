from abc import ABCMeta, abstractmethod
from datetime import date

# hotel_name,nightly_rate,promo_txt,deal_value,deal_type,start_date,end_date

class Deal(object):
  __metaclass__ = ABCMeta

  def __init__(self, rate, txt, dealValue, dealtype, startDate, endDate):
#    self._hotel_name = hotel_name
    self._nightlyRate = rate
    self._promoTxt = txt
    self._dealValue = dealValue
    self._dealType = dealtype
    # startDate = startDate.rstrip()
    # startDate = startDate.lstrip()
    self._startDate = datetime.strptime(startDate, "%Y-%m-%d").date()
    # endDate = endDate.rstrip()
    # endDate = endDate.lstrip()
    self._endDate = datetime.strptime(endDate, "%Y-%m-%d").date()

  @staticmethod
  def getDealType():
    DealType = ['rebate', 'rebate_3plus', 'pct']
    return DealType

  # def getHotelName(self):
  #   return self._hotel_name

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
  factory = staticmethod(factory)
