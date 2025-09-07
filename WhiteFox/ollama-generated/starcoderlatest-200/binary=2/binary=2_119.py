
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        if other is None:
            v1 = self.conv(x1) - 1
        else:
            v1 = self.conv(x1) - other
        return v1


# Initializing the model
m = Model()
other = torch.ones_like(x1)

# Inputs to the model
