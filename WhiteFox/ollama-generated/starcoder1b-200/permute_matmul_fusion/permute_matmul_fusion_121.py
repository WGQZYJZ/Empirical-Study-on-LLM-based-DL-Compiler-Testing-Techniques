
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = self.linear1(v1)
        v4 = torch.nn.functional.relu(self.linear2(v2))
        return torch.cat([v3, v4], dim=2)


# Initializing the model
m = Model()


