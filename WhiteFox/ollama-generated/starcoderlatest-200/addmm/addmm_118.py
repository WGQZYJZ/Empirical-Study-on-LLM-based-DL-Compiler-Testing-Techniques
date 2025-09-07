
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) + inp1  # Add the result of the matrix multiplication to another tensor 'inp'
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
