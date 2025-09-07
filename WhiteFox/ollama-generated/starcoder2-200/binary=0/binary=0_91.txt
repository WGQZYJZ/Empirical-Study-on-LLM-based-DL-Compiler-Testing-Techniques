
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # here we use the keyword argument "other" for addition!
        return v2


# Initializing the model with `other` argument set to a tensor.
m  = Model(other=torch.randn(8,3))
__output__  = m(x1)
