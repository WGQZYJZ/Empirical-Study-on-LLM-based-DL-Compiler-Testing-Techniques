
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if isinstance(other, torch.Tensor):
            v2 = v1 + other
        return v2


m  = Model()
other = torch.randn(103456789, requires_grad=True) # make it gradable just to show a pattern
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1, other=other)

