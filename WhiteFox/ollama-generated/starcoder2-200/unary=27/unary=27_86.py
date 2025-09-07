
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.min = kwargs["min"]
        self.max = kwargs["max"]
 
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, self.min) 
        v3  = torch.clamp_max(v2, self.max)
        return v3

# Initializing the model
m  = Model(**kwargs)

