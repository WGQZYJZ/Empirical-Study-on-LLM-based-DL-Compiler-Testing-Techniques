
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2=None):
        v1 = torch.mm(inp1, inp2) + 0.5
        return v1


# Initializing the model
m = Model()


# Inputs to the model: inp1 and an optional input tensor 'inp' with keyword argument.
__output__, 