
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        v1 = torch.mm(inp1, inp2)
        return v1 + inp
 
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(32, 64)
x2 = torch.randn(32, 64)
