
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1)
        v2  = v1 > 0 
        v4  = torch.where(v2, v1, -v3)
        return v4


# Initializing the model