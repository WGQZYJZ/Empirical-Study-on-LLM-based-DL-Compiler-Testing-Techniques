
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1)
 
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = (v1 > 0).type(torch.bool)
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model