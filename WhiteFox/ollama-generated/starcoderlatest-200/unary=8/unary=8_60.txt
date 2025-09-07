
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transp = torch.nn.ConvTranspose2d(8, 3, 4, stride=4)
 
    def forward(self, x1):
        v1 = self.conv_transp(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = v1 * v3
        v5 = v4 / 6
        return v5
