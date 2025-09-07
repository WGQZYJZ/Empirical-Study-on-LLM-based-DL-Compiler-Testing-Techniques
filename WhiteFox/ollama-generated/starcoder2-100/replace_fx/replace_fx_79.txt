

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v1, dtype=torch.double) # generate a tensor with the same size as input_tensor filled with random numbers 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(50, 784)
