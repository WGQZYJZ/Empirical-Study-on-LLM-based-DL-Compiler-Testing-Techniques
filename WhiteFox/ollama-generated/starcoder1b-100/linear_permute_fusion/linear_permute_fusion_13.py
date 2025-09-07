
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.linear(x1, ...)  # Apply linear transformation to the input tensor.
        v1 = t1.permute(...)  # Permute the output tensor from the linear transformation.
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
