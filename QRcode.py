import qrcode

class myQR:
    def __init__(self,size:int,border:int):
        self.qr = qrcode.QRCode(box_size=size,border=border)
    
    def creat_qr(self,file_name,bg):
        url = input("enter url")

        try:
            self.qr.add_data(url)
            image = self.qr.make_image(back_color = bg)
            image.save(file_name)
            print(f"{file_name} saved")
            
        except:
            Exception
            
def main():
    qr = myQR(size=30,border=2)
    user = str(input("enter name"))
    file_name = f"{user}.png"
    color = str(input("enter BGcolor"))
    qr.creat_qr(file_name=file_name,bg=color)

if __name__ == "__main__":
    main()