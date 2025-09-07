
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.8) # Apply dropout to the input tensor. The probability of dropout is set as '0.8'
        v2 = torch.rand_like(v1, dtype=torch.int32) # Generate a tensor with the same size as v1 filled with random numbers, and cast them into int data type.
        return 5 * x1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3) # An example input tensor for the model
