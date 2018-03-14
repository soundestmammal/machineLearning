price = 100
tax_rate = 0.865

def TaxCalc(price, tax_rate):
	total_tax = price * tax_rate
	new_price =  price + total_tax
	return new_price

TaxCalc(price, tax_rate)