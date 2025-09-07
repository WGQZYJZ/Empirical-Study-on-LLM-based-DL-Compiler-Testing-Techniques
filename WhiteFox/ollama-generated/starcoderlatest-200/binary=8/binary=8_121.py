
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is not None:
            v2 = v1 + other
        else:
            v2 = v1
        return v2

# Initializing the model with additional inputs
m = Model()
m = Model(other=x1)


