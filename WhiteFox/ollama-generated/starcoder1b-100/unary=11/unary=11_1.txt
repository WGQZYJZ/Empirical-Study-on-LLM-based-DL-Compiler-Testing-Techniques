
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = v1.clamp_(0,6) # v2 is the clamped and divided by 6, and v4 is the max value for t4
        v3 = v2 / 6 # V3 is the divided by 6 result of clamping at t2, so v5 = (v3 - t2)/t2 will give the output of the transposed convolution
        return v5


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
