class Factory:
    def __init__(self, material : str, zip : int, pockets : int):
        self.material = material
        self.zips = zip
        self.pocket = pockets


    def show(self):
        print(f"Your object details is for Material: {self.material}, Zip: {self.zips}, Pocket: {self.pocket}")


puma = Factory("leather","ww",2)
reebok = Factory("nylon",22,66)

puma.show()
reebok.show()

