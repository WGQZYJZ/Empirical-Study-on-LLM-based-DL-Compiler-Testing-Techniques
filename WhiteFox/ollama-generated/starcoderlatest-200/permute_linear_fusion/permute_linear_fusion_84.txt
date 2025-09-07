
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.interpolate(x1.permute(0, 2, 1), (48, 64)) # Add an interpolation layer
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 48, 64)
