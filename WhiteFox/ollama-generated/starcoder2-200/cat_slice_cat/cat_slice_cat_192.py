
class Model(torch.nn.Module):
    def __init__(self, size: int = None):
        super().__init__()

        self.conv0 = torch.nn.Conv2d(3,8,5)

        # Initialize size to 1 by default if it is not set
        # in the user interface or passed from an environmental variable
        if not size:
            self.__setattr__("size", random.randint(160000, 999999))

    def forward(self, x):

        t1 = torch.cat([x] * (self.size + 4), dim=2)
        t2 = t1[:, 0:int((t1.shape[3]) / self.__getattr__("size") + 1)]
        t3 = t2[:, 0:int(5 + random.randint(-9, -1))]
        t4 = torch.cat([t1] * int(self.conv0.weight.shape[1]), dim=2)

        return t3

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 5 + random.randint(-9, -1), self.__getattr__("size") / 64 + 0.70)

