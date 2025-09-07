
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, ...)  # Apply linear transformation to an input tensor.
        return v1.permute(0, 2, 1)  # Permute the output tensor from the linear transformation.


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 6)
