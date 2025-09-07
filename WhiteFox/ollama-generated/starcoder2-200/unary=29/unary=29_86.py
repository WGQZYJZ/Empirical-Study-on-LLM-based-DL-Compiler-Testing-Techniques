
class Model(torch.nn.Module):
    def __init__(self, min_=0., max_=1e64):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 5, stride=2)
        self.min_v  = min_
        self.max_v  = max_
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, self.min_v) # [x - self.min_v]
        v3  = torch.clamp_max(v2, self.max_v) # [max(0, x)]
        return v3


# Initializing the model