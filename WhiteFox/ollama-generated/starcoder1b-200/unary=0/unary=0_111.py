
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (v1  ** 2).mul_(0.044715)
        v3 = v2.add_(-1.0)
        v4 = torch.tanh(v3) + 1
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
