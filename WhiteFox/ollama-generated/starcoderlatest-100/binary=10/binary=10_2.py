
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is None:
            return v1
        else:
            return (v1 + other)

# Initializing the model
m2 = Model2()

# Inputs to the model
x1_1  = torch.randn(1, 3, 64, 64) # The input tensor of shape [batch size=1, channels=3, height=64, width=64]
__output2__ = m2(x1_1)

