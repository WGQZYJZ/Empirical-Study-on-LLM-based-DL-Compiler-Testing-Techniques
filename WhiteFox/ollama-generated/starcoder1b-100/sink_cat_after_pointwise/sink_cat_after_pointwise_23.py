
class Model(torch.nn.Module):
    def __init__(self, linear):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, x2], dim=-1)
        v3 = torch.relu(self.linear(v2))

        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(2, 4, 2)
