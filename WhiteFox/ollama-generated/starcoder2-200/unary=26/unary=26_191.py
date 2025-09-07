
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        negative_slope = 0.5
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t2 = (v1 > 0).float()
        t3 = v1 * negative_slope
        v4 = torch.where(t2, v1, t3) # mask, input 1, input 2
        return v4


m  = Model()
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
