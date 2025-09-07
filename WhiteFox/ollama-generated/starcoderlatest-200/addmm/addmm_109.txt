
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp # This line does not work as the keyword argument 'inp' is passed as an extra input to this function
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)
x2 = torch.randn(3, 8, 32, 32)
