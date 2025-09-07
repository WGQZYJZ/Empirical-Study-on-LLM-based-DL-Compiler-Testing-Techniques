
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + inp
        return v6


# Initializing the model and specifying that tensor 'inp' is a keyword argument
m = Model(inp=torch.randn(8))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 3, 64, 64)
