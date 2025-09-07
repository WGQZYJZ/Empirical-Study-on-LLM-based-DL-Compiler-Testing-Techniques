
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1[:, :, None, :]  # Add a new dimension to the input
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)  # Apply linear transformation to the input
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 5, 4)
