
class Model(torch.nn.Module):
    def __init__(self, inp=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.inp = inp
 
    def forward(self, x1, inp):
        v1 = self.conv(x1)
        v2 = v1 * self.inp
        return v2


# Inputs to the model
m1 = Model()  # Create an instance of class Model and initialize its parameters
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
