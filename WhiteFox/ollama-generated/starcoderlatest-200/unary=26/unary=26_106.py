
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 3, 32, stride=8, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        negative_slope = -2.0e-4
        t1 = v1 > 0
        v2 = v1 * negative_slope
        t3 = torch.where(t1, v2, v1)
        return t3
