
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.convtranspose(x)
        v2 = torch.sigmoid(v1)
 
        return v2


m  = Model()
x0 = torch.randn(1, 3, 64, 64)
__output__  = m(x0)

