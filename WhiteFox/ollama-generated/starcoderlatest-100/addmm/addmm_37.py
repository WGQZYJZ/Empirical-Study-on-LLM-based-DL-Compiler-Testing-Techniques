
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1) # Perform matrix multiplication on two input tensors
        v2 = v1 + x1 # Add the result of the matrix multiplication to another tensor 'inp' 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
