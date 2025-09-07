
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is not None:
            v2  = v1 + other
        else:
            v2  = v1
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 1, 64, 64)
