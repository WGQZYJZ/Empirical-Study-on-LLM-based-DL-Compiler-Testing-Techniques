
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=1)
        t2 = t1.view(t1.shape[0], -1)
        return torch.relu(torch.add(t2, t2))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 3)
