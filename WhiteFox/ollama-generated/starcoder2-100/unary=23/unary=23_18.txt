

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.convt = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        return v1

m = Model()
x1 = torch.randn(4, 8, 64, 64)
__output__  = m(x1)


