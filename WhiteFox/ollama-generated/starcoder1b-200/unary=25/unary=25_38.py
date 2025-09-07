
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        v = self.linear(x)
        t1  = v > 0 # Create a boolean tensor where each element is True if the corresponding element in v is greater than 0, and False otherwise
        v2 = v * negative_slope  # Multiply the output of the linear transformation by the negative slope
        return torch.where(t1, v, v2)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(10, 4)
