
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)

    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.relu(v1 + 0.5)


# Initializing the model
m = Model()

