
class Model(torch.nn.Module):
    def __init__(self, min_value = 0.1543286798969737654587291601, max_value = 2.1333333333333333):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, min_value)
        v3  = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model