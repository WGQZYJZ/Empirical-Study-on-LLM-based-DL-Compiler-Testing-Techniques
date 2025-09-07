
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1 = x1.permute(...)
        v2 = torch.nn.functional.linear(v1, ...)  # Apply linear transformation to the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 3)
