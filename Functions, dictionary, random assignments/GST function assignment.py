# input price and gst rate
price = int(input("Enter the price of item: "))
gstRate = int(input("Enter the GST rate: "))

def priceDetails(price, gstRate):
    gst = gstRate/100*price #calculating gst
    totalPrice = price + gst #total price including GST
    cgst = gst / 2
    sgst = gst / 2

    print("Actual price of item: ",price)
    print("Price after CGST: ", price+cgst)
    print("Price after SGST: ", price+sgst)
    print("Total price with GST: ", totalPrice)

res = priceDetails(price, gstRate)