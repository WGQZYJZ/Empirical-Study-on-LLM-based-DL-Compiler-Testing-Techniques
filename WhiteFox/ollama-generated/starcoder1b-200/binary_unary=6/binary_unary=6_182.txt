
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1 = self.linear(x1) - 1 # Subtract a certain value from the result of the linear transformation
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 10)
