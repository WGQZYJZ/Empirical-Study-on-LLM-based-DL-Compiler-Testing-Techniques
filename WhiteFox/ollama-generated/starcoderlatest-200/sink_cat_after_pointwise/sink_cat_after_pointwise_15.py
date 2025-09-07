
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1[:, 0:2], x1[:, 2:4]], dim=1).view(-1, 2)
        v2 = torch.relu(torch.cat([v1, v1], dim=-1))
        return self.linear(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
