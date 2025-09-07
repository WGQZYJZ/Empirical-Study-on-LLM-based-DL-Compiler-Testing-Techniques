
class Model2(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other
        return v2


# Initializing the model and setting its 'other' attribute
m3  = Model2()
m3.other = torch.ones_like(v1)
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

 # Output of the model
__output__  = m3(x1)