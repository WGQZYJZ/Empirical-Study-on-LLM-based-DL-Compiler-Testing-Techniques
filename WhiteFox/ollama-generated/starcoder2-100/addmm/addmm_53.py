
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        return v2


m = Model()
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 8, 7, 7)
 
inp  = torch.randn(4, 8)
outp__output__  = m(x1)(x2)(inp)
