
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Clamp the result of addition operation to a minimum value
        v4  = torch.clamp_max(v3, 6) # Clamp the output of clamped operation to maximum value
        v5  = v1 * v4 # Multiply convolution output by clamped result
        v6  = v5 / 6 # Divide multiplication result by 6
        return v6

# Initializing the model
m = Model()
 
# Inputs for the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)