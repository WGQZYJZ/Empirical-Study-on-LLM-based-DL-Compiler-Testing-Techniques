
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = v1.clamp_min_(min_)
        v3 = v2.clamp_max_(max_)
        return v3


# Initializing the model