
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)

    def forward(self, x1):
       v1 = self.convt(x1)
       v2 = v1 > 0
       v4 = negative_slope * (v1 - 0.)
       v5 = torch.where(v2, v1, v4)
       return v5


# Initializing the model