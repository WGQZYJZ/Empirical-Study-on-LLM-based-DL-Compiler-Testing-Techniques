
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self._other = other
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + self._other
        return v2


# Initializing the model
m = Model(torch.randn(0))
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # Input tensor for the first time
__output_first_time__ = m(x1)
x2  = torch.randn(1, 8, 64, 64) # Input tensor to test if the model is changed by changing the other parameter
__output_second_time__ = m(x2)

