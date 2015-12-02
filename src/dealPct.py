from datetime import date
import deal

class DealPct(Deal):

  # def DealPct(hotel, rate, txt, dealValue, dealtype, startDate, endDate):
  #   super(hotel, rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    return (rsv.getCheckin() > self._startDate) and (rsv.getCheckin() < self._endDate)

  def getDiscount(self, rsv):
    if (isApplicable(rsv)):
      return (self._dealValue/100)* self._nightlyRate * rsv.getNights()
    else:
      return 0

