
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).float()
        negative_slope = 0.1
        v3 = v1 * negative_slope
        t4 = torch.where(v2, v1, v3)
        return t4
