
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        x2 = torch.cat([x1, x1, ...], dim=0)
        return torch.relu(torch.mean(self.linear(x2)))

# Inputs to the model
x1 = torch.randn(1, 3, 3)
