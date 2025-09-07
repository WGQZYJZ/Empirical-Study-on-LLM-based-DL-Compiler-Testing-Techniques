
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.conv.weight, self.conv.bias)
        v2 = torch.cat([v1], dim=dim)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
