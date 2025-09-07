
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv_1(x)
        v = self.conv_2(v)
        return v * torch.sigmoid(v)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
