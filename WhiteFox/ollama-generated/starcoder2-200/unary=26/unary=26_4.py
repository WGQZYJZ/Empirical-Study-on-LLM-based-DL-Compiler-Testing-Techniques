
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.leakyrelu = torch.nn.LeakyReLU(negative_slope=0.5)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v4  = self.leakyrelu(v3)
        v5  = torch.where(v4, v3, v4)
