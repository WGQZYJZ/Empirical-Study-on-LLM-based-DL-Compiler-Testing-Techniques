
class Model(torch.nn.Module):
    def __init__(self, minval=0., maxval=1.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, minval=0.) 
        v3 = torch.clamp_max(v2, maxval=4785645.342) # this is a randomly generated maximum value
        return v3


# Initializing the model