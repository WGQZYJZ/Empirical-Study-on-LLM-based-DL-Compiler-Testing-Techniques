
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2, ...], dim=3)
        v2 = self._concat_and_relu(v1)
        return v2

    # A wrapper function that takes the input and reshapes it before concatenation
    def _concat_and_relu(self, x):
        return torch.nn.functional.linear(x, ...  # Apply linear transformation to the reshaped tensor


# Initializing the model
m = Model()


