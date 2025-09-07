
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = kwargs["other"]
 
    def forward(self, x):
        v0 = self.other
        v1 = self.conv(x)
        return v1 + v0


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1, other=torch.randn(2))
 
