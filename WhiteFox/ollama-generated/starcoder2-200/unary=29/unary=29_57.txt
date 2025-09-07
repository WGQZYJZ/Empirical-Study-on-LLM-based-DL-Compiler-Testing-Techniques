
class Model(torch.nn.Module):
    def __init__(self, minval=-100., maxval=100.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
        self.max_value = maxval
        self.min_value = minval
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, self.min_value)
        return torch.clamp_max(v2, self.max_value)


# Initializing the model with min/max values of -5 and 70
m = Model(-5., 70.)
 
# Inputs to the model that are not within those values should raise an error
x1 = torch.randn(1,3,64,64)

try:
    __output__  = m(x1)
except AssertionError as e: 
    print("Expected error was raised: ", str(e))

