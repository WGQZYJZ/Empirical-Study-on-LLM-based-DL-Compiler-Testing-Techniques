
class Model(torch.nn.Module):
    def __init__(self, t120200274=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = None if t120200274 is None else t120200274
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other
        return v1


# Initializing the model