
class Model(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.relu(torch.cat([v1, x2], dim=0))
        return torch.relu(torch.cat([x2, self.linear(v2)], dim=0))


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 2, 2)
