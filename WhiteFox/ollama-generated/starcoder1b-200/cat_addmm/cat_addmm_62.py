
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 6)
        self.fc2 = torch.nn.Linear(8, 3)

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.cat([v1, torch.zeros_like(v1)], dim=1)
        return self.fc2(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
