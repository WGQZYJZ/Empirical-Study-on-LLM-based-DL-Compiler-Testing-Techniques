
class Model(torch.nn.Module):
    def __init__(self, conv_shape, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(*conv_shape)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model((3, 64, 64), torch.tensor([5], dtype=torch.float)) # Use a tensor to replace a scalar


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
