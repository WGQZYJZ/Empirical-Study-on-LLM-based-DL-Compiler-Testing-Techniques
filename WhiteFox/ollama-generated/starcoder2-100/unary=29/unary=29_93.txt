
class Model(torch.nn.Module):
    def __init__(self, min_=0., max_=1e3):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 4, 5)
        self._min_ = min_ 
        self._max_ = max_
        
    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = torch.clamp_min(v1, min_)
         v3 = torch.clamp_max(v2, max_)
         return v3
 
# Initializing the model