
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if other:
            v2 = v1 + other
        else:
            v2 = v1 + 0
        return v2


# Initializing the model
m = Model()
m2 = Model(torch.tensor([0,0,1,1]))
__output_1__ = m(x1)
__output_2__ = m2(x1)

