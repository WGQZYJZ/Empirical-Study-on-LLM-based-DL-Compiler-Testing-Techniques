
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


# Keyword argument "other" with a random value from normal distribution and dtype equal to input tensor's dtype and device equal to input tensor's device
other = torch.rand(8).to(x1.device) * (0.9 - 0.3) + 0.3 


