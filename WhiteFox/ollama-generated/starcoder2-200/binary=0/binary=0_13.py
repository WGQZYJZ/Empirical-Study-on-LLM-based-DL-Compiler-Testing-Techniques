
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other 
        return v2
 
# Initializing the model with a constant tensor of size [64] as an argument to the keyword argument "other"
m  = Model(torch.Tensor([0., 1., ..., 63.]))


# Inputs to the model