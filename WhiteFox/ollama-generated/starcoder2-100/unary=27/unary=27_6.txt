
class Model(torch.nn.Module):
    def __init__(self, min_, max_=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.min  = min_
        self.max  = (
            self.conv if not max else 
            torch.nn.functional.clamp_max(self.conv, max_)
        )
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, self.min)
        return torch.clamp_max(v2, self.max)


# Initializing the model