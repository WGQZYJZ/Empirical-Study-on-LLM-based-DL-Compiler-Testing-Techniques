
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        v1 = t1.view(-1, 2)
        t2 = torch.relu(v1)
        return self.linear(t2).reshape(-1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
