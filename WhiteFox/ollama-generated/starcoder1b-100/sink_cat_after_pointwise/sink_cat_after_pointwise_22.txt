
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.view(-1, 2)
        t1 = self.linear(v1)
        return torch.relu(t1)


# Inputs to the model
x1 = torch.randn(1, 2)
