
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, bias=False)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if type(v1) is not torch.Tensor:
            v1 = torch.ones_like(v1) * v1

        if v1.shape != x1.shape:
            raise Exception()
 
        v2 = v1 - other
        return v2


# Initializing the model
m = Model(5.0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
