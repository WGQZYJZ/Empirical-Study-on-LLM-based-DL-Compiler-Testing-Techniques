
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convt = torch.nn.ConvTranspose1d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = (v1 > 0).float() * negative_slope
        return v2


# Initializing the model