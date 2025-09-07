
class Model(torch.nn.Module):
    def __init__(self, b):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.b = torch.nn.Parameter(torch.zeros(()), requires_grad=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - self.b
        return v2


# Initializing the model
m  = Model(0.5)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)