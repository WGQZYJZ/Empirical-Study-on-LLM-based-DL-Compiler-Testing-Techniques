
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2=None):
        v1 = torch.mm(inp1, inp2)
        v2  = v1 + inp
 
m = Model()

