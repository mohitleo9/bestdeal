from datetime import datetime

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

class Deal(object):

  def __init__(self, rate, txt, dealValue, dealtype, startDate, endDate):
    self._nightlyRate = rate
    self._promoTxt = txt
    self._dealValue = (-1) * dealValue
    self._dealType = dealtype
    self._startDate = datetime.strptime(startDate, "%Y-%m-%d").date()
    self._endDate = datetime.strptime(endDate, "%Y-%m-%d").date()

  def getValue(self):
    return self._dealValue

  def getnightlyRate(self):
    return self._nightlyRate

  def getPromoTxt(self):
    return self._promoTxt

  def isApplicable(self, rsv):
    print "hello"
    return (rsv.getCheckin() > self._startDate) and (rsv.getCheckin() < self._endDate)


  def getDiscount(self, rsv):
    print "hey!!"
    pass


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
    print "chk 1"
    print "pct", super(Deal, self).isApplicable(self, rsv)
    print "chk 2"
    return super(Deal, self).isApplicable(self, rsv)

  def getDiscount(self, rsv):
    val = super(Deal, self).getValue(self)
    rate = super(Deal, self).getnightlyRate(self)
    discount = (val/100.0) * (rate * rsv.getNights())
    return discount

class DealRebate(Deal):

  def __init__(rate, txt, dealValue, dealtype, startDate, endDate):
    super(Deal, self).__init__(rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    print "chk 3"
    print "rebate", super(Deal, self).isApplicable(self, rsv)
    print "chk 4"
    return super(Deal, self).isApplicable(self, rsv)

  def getDiscount(self, rsv):
    discount = super(Deal, self).getValue(self)
    return discount

class DealRebate3Plus(Deal):

  def __init__(rate, txt, dealValue, dealtype, startDate, endDate):
    super(Deal, self).__init__(rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    print "chk 5"
    print "3plus", super(Deal, self).isApplicable(self, rsv)
    print "chk 6"
    return super(Deal, self).isApplicable(self, rsv) and (rsv.getNights() >= 3)

  def getDiscount(self, rsv):
    discount = super(Deal, self).getValue(self)
    return discount
