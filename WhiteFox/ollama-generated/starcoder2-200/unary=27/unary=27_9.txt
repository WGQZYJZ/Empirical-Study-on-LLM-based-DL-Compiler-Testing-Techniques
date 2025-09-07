
class Model(torch.nn.Module):
    def __init__(self, max=1000):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self._max = max

    @property 
    def max(self):
        return self._max
 
    @max.setter  
    def max(self, value):
        self._max = value
        
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -float(self._max))
        v3  = torch.clamp_max(v2, float(self._max))
        return v3


# Initializing the model