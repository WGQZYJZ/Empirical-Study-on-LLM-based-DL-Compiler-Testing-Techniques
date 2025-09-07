
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
