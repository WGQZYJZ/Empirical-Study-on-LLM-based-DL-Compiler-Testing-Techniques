
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
inp1 = torch.randn(3072)
inp2 = torch.randn(5888)
