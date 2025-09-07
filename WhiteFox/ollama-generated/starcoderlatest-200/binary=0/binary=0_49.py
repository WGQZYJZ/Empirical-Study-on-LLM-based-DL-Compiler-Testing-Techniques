
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._other = torch.nn.Parameter(data=torch.Tensor(other_tensor))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._other
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
