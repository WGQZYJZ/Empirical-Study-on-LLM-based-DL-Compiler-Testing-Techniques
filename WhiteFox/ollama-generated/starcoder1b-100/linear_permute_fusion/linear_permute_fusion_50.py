
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 1)

    def forward(self, x):
        v = torch.nn.functional.relu(x @ self.linear.weight + self.linear.bias)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 4)
