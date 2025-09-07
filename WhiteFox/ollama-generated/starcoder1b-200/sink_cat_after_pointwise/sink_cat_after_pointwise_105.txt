
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 1, 2)
        v2 = torch.cat([v1, x2], dim=2).reshape(-1, 3)
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

