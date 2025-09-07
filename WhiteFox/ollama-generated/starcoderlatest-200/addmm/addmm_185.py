
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) # Perform matrix multiplication on two input tensors
        return v1 + inp


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
