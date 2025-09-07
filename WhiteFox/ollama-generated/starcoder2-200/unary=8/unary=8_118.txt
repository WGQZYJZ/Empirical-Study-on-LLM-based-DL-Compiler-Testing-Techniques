
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = F.clamp(v1, min=0)
        v3  = F.clamp(v2, max=6)
        v4  = v1 * v3
        return torch.div(v4, 6)

m = Model()

