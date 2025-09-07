
class Model(torch.nn.Module):
    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        min_v  = x1 * min_value
        max_v  = x1 * max_value
        clamp_v = torch.clamp(v1, min_value=min_v, max_value=max_v)
        return clamp_v


# Initializing the model
m = Model(min_value=0, max_value=1)


