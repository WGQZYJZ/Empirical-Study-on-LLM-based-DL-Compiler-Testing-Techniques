
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None): # If no value for 'x2' is specified, it defaults to None
        v1 = torch.mm(x1, x1)  # Matrix multiplication of two input tensors
        v2 = v1 + inp if x2 == None else v1 + x2 # Add the result of the matrix multiplication to another tensor
        return v2
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3)
