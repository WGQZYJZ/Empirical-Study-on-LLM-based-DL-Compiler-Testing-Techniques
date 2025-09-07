
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3,8 ,16, 4)
 
        self.batchnorm = nn.BatchNorm2d(8)
 
    def forward(self, x0):
        y0 = self.conv(x0)
 
        z0 = y0 * torch.sigmoid(y0)
 
        return z0


m = Model()
 
input1  = torch.randn(4,3,657,283)
output1 = m(input1)

