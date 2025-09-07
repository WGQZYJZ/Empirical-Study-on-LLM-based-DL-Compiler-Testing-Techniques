
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other): # the keyword argument here is "other"
        v1  = self.conv(x1)
        v2  = v1 + other  # This tensor has to be passed as a keyword arg.
        return v2


# Initializing the model