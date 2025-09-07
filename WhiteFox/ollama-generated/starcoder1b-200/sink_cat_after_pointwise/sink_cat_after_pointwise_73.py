
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 2)
        return torch.relu(t2 * (x3 + 1))


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2)
