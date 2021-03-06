from datetime import datetime


class Reservation(object):
  def __init__(self, hotel, checkinDate, nights):
    self.hotel = hotel
    self.checkin = checkinDate
    self.nights = int(nights)

  def get_checkin(self):
    return self.checkin

  def get_hotel(self):
    return self.hotel

  def get_nights(self):
    return self.nights


class Deal(object):
  def __init__(self, rate, txt, dealValue, dealtype, startDate, endDate):
    self._nightlyRate = int(rate)
    self._promoTxt = txt
    self.dealValue = (-1) * float(dealValue)
    self._dealType = dealtype
    self._startDate = datetime.strptime(startDate, "%Y-%m-%d").date()
    self._endDate = datetime.strptime(endDate, "%Y-%m-%d").date()

  def getnightlyRate(self):
    return self._nightlyRate

  def getPromoTxt(self):
    return self._promoTxt

  def isApplicable(self, rsv):
    return (rsv.get_checkin() > self._startDate) and (rsv.get_checkin() < self._endDate)


  def getDiscount(self, rsv):
    pass


  @classmethod
  def factory(cls, rate, txt, dealValue, dealtype, startDate, endDate):
    if dealtype == "rebate":
      return DealRebate(rate, txt, dealValue, dealtype, startDate, endDate)
    elif dealtype == "rebate_3plus":
      return DealRebate3Plus(rate, txt, dealValue, dealtype, startDate, endDate)
    elif dealtype == "pct":
      return DealPct(rate, txt, dealValue, dealtype, startDate, endDate)


class DealPct(Deal):

  def isApplicable(self, rsv):
    return super(DealPct, self).isApplicable(rsv)

  def getDiscount(self, rsv):
    val = self.dealValue
    rate = self.getnightlyRate()
    discount = (val / 100.0) * float(rate * rsv.get_nights())
    return discount

class DealRebate(Deal):

  def getDiscount(self, rsv):
    discount = self.dealValue
    return discount

class DealRebate3Plus(Deal):

  def isApplicable(self, rsv):
    val = super(DealRebate3Plus, self).isApplicable(rsv)
    return val and rsv.get_nights() >= 3

  def getDiscount(self, rsv):
    discount = self.dealValue
    return discount
