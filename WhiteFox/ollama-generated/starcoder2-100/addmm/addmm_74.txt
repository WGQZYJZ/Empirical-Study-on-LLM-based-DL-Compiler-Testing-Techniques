
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Performs matrix multiplication on two tensors x1 and x2
        v3 = v1 + inp  # Adds the result of the matrix multiplication to another tensor 'inp'
        return v3

# Initializing the model with keyword argument for 'inp' tensor
m = Model()


# Inputs to the model
x1  = torch.randn(4, 5)
x2 = x1[:, :2] # Extracting a submatrix of the first input tensor
__inp__ = torch.zeros(6) # Creating the 'inp' tensor with shape (3,)

