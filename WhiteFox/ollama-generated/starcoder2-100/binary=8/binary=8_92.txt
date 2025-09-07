
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, y=None):
        v1 = self.conv(x1)
        if not y is None:
            v1 += y
        return v1


m  = Model()
__output__  = m(torch.randn(1, 3, 64, 64))