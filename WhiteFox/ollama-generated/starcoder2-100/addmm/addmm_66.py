
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) # Matrix multiplication
        v2  = v1 + inp
        return v2


# Initializing the model with keyword argument
m  = Model()

# Inputs to the model