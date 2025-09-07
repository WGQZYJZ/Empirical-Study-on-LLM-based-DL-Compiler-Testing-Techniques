
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        if inp is None:
            # Generate random input tensors
            t1 = torch.randn(*x1.shape)
            # Use the tensor for matrix multiplication 't1' with 'x2'
            v1 = torch.mm(t1, x2)
        else:
            v1 = torch.mm(inp, x2)
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 8)
