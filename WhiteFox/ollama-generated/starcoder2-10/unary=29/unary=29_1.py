

class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()

        self._min = kwargs['min'] # 4
        self._max = kwargs['max'] # 32
 
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
    
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.clamp_min(v1, self._min) # 4
        v3 = torch.clamp_max(v2, self._max) # 32
        return v3


# Initializing the model with 4 and 32 as the minimum/maximum clamping values
m = Model(
    min=4, 
    max=32
)


