
class Model(torch.nn.Module):
    def __init__(self, t):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.t = t

    def forward(self, x1):
        v1 = self.conv(x1) + self.t

        return v1
# Initializing the model with a keyword argument passed as an argument to the `Model` class:

 # Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)
