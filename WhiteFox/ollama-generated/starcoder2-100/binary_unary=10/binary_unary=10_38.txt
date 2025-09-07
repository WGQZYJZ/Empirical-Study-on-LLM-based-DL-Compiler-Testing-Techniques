
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256*10, 7)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1


m = Model()
x1  = torch.randn(32, 256)
other = torch.zeros_like(x1)
__output__  = m(x1 + other)

