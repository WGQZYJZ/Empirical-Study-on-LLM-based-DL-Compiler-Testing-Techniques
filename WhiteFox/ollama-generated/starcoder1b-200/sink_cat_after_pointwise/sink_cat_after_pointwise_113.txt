
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.linear = torch.nn.Linear(..., ...)

    def forward(self, x1):
        return x2 @ self.linear(...)  # The `@` is a matrix multiplication operator, and the two input tensors are assumed to be of size '(..., dim)'


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, ..., dim)  # Assume dim=2
__output = m(x1)


