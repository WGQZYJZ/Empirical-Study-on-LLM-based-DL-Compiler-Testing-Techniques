
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1)  # Invoke dropout on the input tensor
        v2 = torch.rand_like(v1)              # Generate a random tensor with the same shape and type as the input tensor
        return torch.add(v1, v2)               # Return sum of these two tensors


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(3, 4)                     # An input tensor with 50% probability being masked by 0s and 50% keeping its original values

