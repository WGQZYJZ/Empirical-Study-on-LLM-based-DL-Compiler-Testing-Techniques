

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = (v1 > 0).to(torch.float32) # mask where values are greater than zero
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3 )# return values based on mask
        return v4

m = Model()
x1 = torch.randn(10,8,65,65)
__output__= m(x1)

