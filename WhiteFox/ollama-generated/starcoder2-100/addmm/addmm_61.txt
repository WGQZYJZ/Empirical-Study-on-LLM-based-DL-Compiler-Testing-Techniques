
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None):
        v1 = torch.mm(x1, torch.randn(32, 8))
        v2 = v1 + inp 
        return v2


m = Model()
__output___ = m(inp=torch.randn(32, 8))


