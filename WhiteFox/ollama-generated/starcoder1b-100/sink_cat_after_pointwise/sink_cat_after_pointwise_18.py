
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        t1 = torch.cat([v1, ...], dim=2)
        t2 = t1.view(-1)
        return torch.relu(t2)


# Initializing the model
m = Model()

