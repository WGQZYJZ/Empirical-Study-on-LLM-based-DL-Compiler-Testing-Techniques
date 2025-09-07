
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
        self.leakyrelu = torch.nn.LeakyReLU(negative_slope=0.5)
 
    def forward(self, x):
        v1 = self.convt(x)
        v2 = v1 > 0
        v3 = -v1
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model