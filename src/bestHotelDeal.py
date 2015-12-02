import sys
from datetime import datetime
import csv
from allDealClasses import Deal, Reservation


class BestHotelDeal(object):
  def __init__(self):
    self.deal_hash_table = {}
    self.cmd_args = []
    self.FILENAME = ''
    self.rsv = None
    self.best = 0
    self.best_deal = None

  def readCmdArgs(self, argms):
    self.cmd_args = argms
    self.FILENAME = self.cmd_args[1]
    HOTEL = self.cmd_args[2]
    CHECKIN = datetime.strptime(self.cmd_args[3], "%Y-%m-%d").date()
    NIGHTS = int(self.cmd_args[4])
    self.rsv = Reservation(HOTEL, CHECKIN, NIGHTS)
#    print self.cmd_args

  def read_store_deals(self):
    with open(self.FILENAME, 'rb') as f:
      reader = csv.reader(f)
      hotelDeals = list(reader)

    for deal_args in hotelDeals[1:]:
#      print self.deal_hash_table
      print deal_args
      curr_deal = None
      curr_deal = Deal.factory(deal_args[1], deal_args[2], deal_args[3], deal_args[4], deal_args[5], deal_args[6])
      if deal_args[0] in self.deal_hash_table:
        self.deal_hash_table[deal_args[0]].append(curr_deal)
      else:
        self.deal_hash_table[deal_args[0]] = []
        self.deal_hash_table[deal_args[0]].append(curr_deal)

  def findBestDeal(self):
    # print "rsv hotel", self.rsv.hotel
    for hotel_deal in self.deal_hash_table[self.rsv.hotel]:
      if (hotel_deal.isApplicable(self.rsv)):
        discount = hotel_deal.getDiscount(self.rsv)
        if (discount>self.best):
            self.best = discount
            self.best_deal = hotel_deal

  def getDealHashTable(self):
    return self.deal_hash_table

  def getCmdArgs(self):
    return self.cmd_args

  def getFilename(self):
    return self.FILENAME

  def getReservation(self):
    return self.rsv

  def getBestDeal(self):
    if self.best_deal is not None:
      return self.best_deal._promoTxt
    else:
      return 'None'


def main():
  print sys.argv
  bestDeal = BestHotelDeal()
  bestDeal.readCmdArgs(sys.argv)
  bestDeal.read_store_deals()
  bestDeal.findBestDeal()

  result = bestDeal.getBestDeal()
  print result


if __name__ == '__main__':
  main()
