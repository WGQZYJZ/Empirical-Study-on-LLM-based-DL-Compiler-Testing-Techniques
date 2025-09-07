
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[:, 0:3], x2) # Matrix multiplication of two input tensors
        v2 = v1 * 5 + v1  # Matrix multiplication result multiplied by a constant and then added to the matrix multiplication result twice
        return v2

# Initializing the model
m = Model()
x1, x2 = torch.randn(4096), torch.randn(3, 784)

# Inputs to the model
x1 = [torch.randn(125) for i in range(5)] + [None] # To ensure that the list is of a length other than one and not NoneType. This list is used as an input tensor
__output__  = m(*x1, x2)

