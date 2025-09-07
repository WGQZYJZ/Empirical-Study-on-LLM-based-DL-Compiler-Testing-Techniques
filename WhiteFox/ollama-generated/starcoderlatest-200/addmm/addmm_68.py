
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, inp):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, x2) # Matrix multiplication
        return (v2 + inp).max()


# Initializing the model
m = Model()
# Inputs to the model
inp = torch.randn(3, 3, 64, 64)
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
