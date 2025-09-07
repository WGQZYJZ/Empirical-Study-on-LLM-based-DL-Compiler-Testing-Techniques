
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2) # Perform matrix multiplication on two input tensors
        v2 = v1 + inp
        return v2

# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(16)  # Shape: (B,)
x1 = torch.randn(1, 32, 32)
x2 = torch.randn(1, 32, 32)
