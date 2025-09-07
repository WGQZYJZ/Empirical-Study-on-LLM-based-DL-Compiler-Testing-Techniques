
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1) 
        v2 = torch.gt(v1, 0) # mask, v1 is the output of conv_transpose
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) 
        return v4

m  = Model()
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

