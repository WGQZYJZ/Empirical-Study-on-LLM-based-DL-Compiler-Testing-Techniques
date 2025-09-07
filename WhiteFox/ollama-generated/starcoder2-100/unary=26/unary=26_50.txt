
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1  = self.conv(x)
        mask = (v1 > 0).type(torch.cuda.FloatTensor)
        v2  = v1 * self.negative_slope 
        v3  = torch.where(mask, v1, v2)
        return v3


m = Model()

x1  = torch.randn(1, 3, 64, 64).cuda()
__output__  = m(x1)