
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)
        v1 = t1.view([-1])
        v2 = torch.relu(v1)
        return self.linear(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 4, 5)
