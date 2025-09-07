
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)

    def forward(self, x):
        return self.linear(x).reshape(-1, 2) - x


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 8)
