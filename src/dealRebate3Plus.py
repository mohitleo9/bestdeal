from datetime import date
import deal

class DealRebate3Plus(Deal):

  # def DealRebate3Plus(hotel, rate, txt, dealValue, dealtype, startDate, endDate):
  #   super(hotel, rate, txt, dealValue, dealtype, startDate, endDate)

  def isApplicable(self, rsv):
    return (rsv.getCheckin() > self._startDate) and (rsv.getCheckin() < self._endDate) and (rsv.getNights() >= 3)

  def getDiscount(self, rsv):
    if (isApplicable(rsv)):
      return self._dealValue
    else:
      return 0
