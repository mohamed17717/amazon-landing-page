from random import choice
from string import printable
printable = printable.split(' ')[0]

def random_string(length=15):
  return ''.join( [choice(printable) for _ in range(length)] )


def calcPriceAfterSale(salePercent, orginalPrice):
  sale = salePercent*orginalPrice/100
  return orginalPrice - sale