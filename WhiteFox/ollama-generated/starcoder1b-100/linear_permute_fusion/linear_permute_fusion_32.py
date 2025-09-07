
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        return torch.relu(self.linear(x1))


# Initializing the model
m = Model()
x1 = torch.randn(4, 2, 3)
