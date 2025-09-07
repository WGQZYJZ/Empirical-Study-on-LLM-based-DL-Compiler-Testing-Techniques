
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = torch.clamp(v1, min=0, max=6)
        v3  = v1 * v2
        v4  = v3 / 6 
        return v4

m  = Model()
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

