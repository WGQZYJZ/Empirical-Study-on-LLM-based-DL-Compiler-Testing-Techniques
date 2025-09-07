
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8096, 3072, requires_grad=True)
x2 = torch.randn(4048, 3072, requires_grad=True)
