
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = float(other)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other  # 'other' can be either a tensor or a scalar
        return v2


# Initializing the model with input tensor of shape `[B, 3, H, W]` and `other` being 0:
m = Model(0)
x1_0 = torch.randn(4, 3, 64, 64) # input is random float numbers
__output___  = m(x1_0)


# Initializing the model with input tensor of shape `[B, 3, H, W]` and `other` being a 5-D tensor:
m = Model()
x1_1 = torch.randn(4, 3, 64, 64) # input is random float numbers
other = torch.randn(2, 3, 5, 7, 8).to(dtype=torch.float32) # 5-D tensor of shape [2, 3, 5, 7, 8]
__output___1  = m(x1_1, other)


# Initializing the model with input tensor of shape `[B, 3, H, W]` and `other` being a scalar:
m = Model()
x1_2 = torch.randn(4, 3, 64, 64) # input is random float numbers
other = 5.0  # scalar value
__output___2  = m(x1_2, other)

