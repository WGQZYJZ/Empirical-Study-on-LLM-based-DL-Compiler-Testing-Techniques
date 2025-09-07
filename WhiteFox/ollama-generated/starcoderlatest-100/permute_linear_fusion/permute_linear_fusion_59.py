
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(...) # Permute the input tensor with more than 2 dimensions. The permuted tensor should be used for linear transformation.

        return torch.nn.functional.linear(v1, ...)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(...) # generate a random input tensor with more than 2 dimensions
