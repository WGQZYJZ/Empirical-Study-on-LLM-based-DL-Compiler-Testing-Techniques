
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) # Perform matrix multiplication on two input tensors
        v2 = v1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
