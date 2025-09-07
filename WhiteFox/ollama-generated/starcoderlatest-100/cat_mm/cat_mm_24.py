
class Model(torch.nn.Module):
    def __init__(self, c1=32, c2=64):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(c1, c1, 1) 
        self.conv_2 = torch.nn.Conv2d(c1, c2, 1) 
    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.conv_2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
__input__1 = torch.randn(3, 64, 64)
__output__2 = m(__input__1)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 32, 7, stride=2, padding=3) 
        self.conv_2 = torch.nn.Conv2d(32, 64, 5, stride=1, padding=2) 
    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.conv_2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
__input__3 = torch.randn(1, 3, 64, 64)
__output__4 = m(__input__3)

