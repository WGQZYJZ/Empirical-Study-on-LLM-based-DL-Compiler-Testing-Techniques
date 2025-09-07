
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self.other = torch.nn.Parameter(torch.randn(*other.shape))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.other is not None:
            v2 = v1 + self.other
        else:
            v2 = v1
        return v2


# Initializing the model
m = Model()
__init__()