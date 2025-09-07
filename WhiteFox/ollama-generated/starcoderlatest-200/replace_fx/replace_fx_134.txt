
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(x1, ...) # Generate a tensor with the same size as input_tensor filled with random numbers
        v2 = torch.nn.functional.dropout(v1, 0.2) # Apply dropout to the random tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 5)
