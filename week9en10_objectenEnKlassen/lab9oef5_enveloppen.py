class Envelop():
    def __init__(self, weight, sent=False):
        self.weight = weight
        self.sent = sent
        self.costCalculated = False
        self.franked = False
        self.costMultiplier = 10

    def send(self):
        if (self.franked == True):
            self.sent = True
            print("letter succesfully sent")
        else:
            print("you first need to frank this envelope before you can send it")
    
    def frank(self, postageCosts):
        if (self.costCalculated == True):
            cost = self.needs_postage_costs()
            if (postageCosts == cost):
                self.franked = True
            else:
                print(f"insufficient postage: need €{cost - postageCosts} more")
        else:
            print("you need to calculate postage before you can frank")

    def needs_postage_costs(self):
        self.costCalculated = True
        return (self.weight * self.costMultiplier)

class GroteEnvelop(Envelop):
    def __init__(self, weight, sent=False):
        super().__init__(weight, sent)
        self.costMultiplier=15
    
dinges = Envelop(15.2)
dinges.send()
dinges.frank(5)
print(f"postage costs: €{dinges.needs_postage_costs()}")
dinges.send()
dinges.frank(13)
dinges.frank(152)
dinges.send()

print("\n")

megaDinges = GroteEnvelop(15.2)
megaDinges.send()
megaDinges.frank(5)
print(f"postage costs: €{megaDinges.needs_postage_costs()}")
megaDinges.send()
megaDinges.frank(13)
megaDinges.frank(228)
megaDinges.send()
    