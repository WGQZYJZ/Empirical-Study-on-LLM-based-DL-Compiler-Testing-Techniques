
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        return torch.relu(v1 + other)


# Initializing the model
m = Model()


