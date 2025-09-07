
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1, device=device) # Generate a tensor with the same size as input_tensor filled with random numbers on the given device (CPU by default)
        v3  = torch.nn.functional.dropout(v2, ...) # Apply dropout to the generated random tensor. The argument  ...  is not used and will be erased from the graph of the model.
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2)

