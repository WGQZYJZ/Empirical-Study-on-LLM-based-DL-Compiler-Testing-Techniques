
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 3, 4, 5, ...)  # Permute the output tensor from the linear transformation with more than 5 dimensions
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, ..., 3)
