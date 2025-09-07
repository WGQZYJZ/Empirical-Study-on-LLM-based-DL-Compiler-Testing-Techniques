
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, inp) + inp
        return v2

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(8, 3, 64, 64)
