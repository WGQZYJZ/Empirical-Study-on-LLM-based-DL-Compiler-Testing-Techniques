
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None):
        v1 = torch.mm(inp1[0], 3) 
        v2 = v1 + inp1[1]
        return v2
# Initializing the model
m = Model()
 
__inputs__ = [torch.randn((4, 4)), torch.randn((5))]
