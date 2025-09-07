
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1  = self.conv(x1) + other
        return v1


m = Model()
x1  = torch.randn(1, 3, 64, 64)
other  = torch.randn_like(x1) # random tensor with same shape and dtype as x1
__output__  = m(x1, other=other)

