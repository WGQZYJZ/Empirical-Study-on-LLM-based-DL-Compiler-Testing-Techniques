
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Matrix multiplication on two tensors
        inp = v1 + 3 # Add the result of matrix multiplication to a tensor with value `3`
        return inp


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 5) # shape: (10, 5)
x2 = torch.randn(5, 10) # shape: (5, 10)
