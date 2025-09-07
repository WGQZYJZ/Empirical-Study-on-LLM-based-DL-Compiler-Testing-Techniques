
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        v1 = torch.nn.functional.linear(x1, ...)  # Apply linear transformation to the input tensor and the optional second argument.
        v2 = x2.permute(...)  # Permute the output tensor from the linear transformation.

        return (v1, v2)


# Initializing the model
m = Model()

