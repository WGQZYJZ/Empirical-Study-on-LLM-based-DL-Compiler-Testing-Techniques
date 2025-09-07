
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
        # Min/max values to clamp the convolution output to
        self.min   = min_
        self.max   = max_

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, self.min)
        v3  = torch.clamp_max(v2, self.max)
        return v3

# Initializing the model with the min/max values provided as keyword arguments to the model class constructor
m = Model(40., -5.)


# Inputs to the model