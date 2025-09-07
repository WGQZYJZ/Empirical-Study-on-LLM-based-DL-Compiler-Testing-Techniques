
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.cat([x1, x1, ...], dim=...)
        t2 = t1.view(-1, 2)
        return torch.relu(t2)


# Initializing the model
m = Model()


