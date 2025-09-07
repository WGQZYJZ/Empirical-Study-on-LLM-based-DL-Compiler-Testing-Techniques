
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.8) # Apply dropout to the input tensor
        t2 = torch.rand_like(t1) # Generate a random tensor with the same size as `t1` filled with random numbers
        return t2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 5)
__output__= m(x1)

