
class Model2(torch.nn.Module):
    def __init__(self, conv: torch.nn.Conv2d,  other = None):
        super().__init__()
        self.conv = conv
        self._other  = other
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 - self._other
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output_1__  = m(x1)
__other___  = torch.randn(128, 1024, 7, 7)
m = Model(conv, __other__)
__output_2__  = m(x1)

