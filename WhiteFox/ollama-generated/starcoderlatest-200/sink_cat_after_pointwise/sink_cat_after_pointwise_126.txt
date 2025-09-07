
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=2)
        v2 = v1.view(-1, 4)
        v3 = torch.relu(v2)
        return self.linear(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 3)
