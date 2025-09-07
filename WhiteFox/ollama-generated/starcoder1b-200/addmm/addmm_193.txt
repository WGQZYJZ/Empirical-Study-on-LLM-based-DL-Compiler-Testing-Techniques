
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2)
 
    def forward(self, x1, inp):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2 + inp


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
inp = torch.randn(1, 8, 32, 32)
