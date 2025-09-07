

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v2  = self.linear(x1)
        v3  = v2 + 3
        v4  = torch.clamp_min(v3,0)
        v5  = torch.clamp_max(v4,6)
        return v5/6


m = Model()
x1  = torch.randn(1, 3)
__output__  = m(x1)
