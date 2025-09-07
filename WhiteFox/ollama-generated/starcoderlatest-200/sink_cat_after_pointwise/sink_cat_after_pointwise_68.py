
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = torch.relu(v1).view(-1, 64, 1)
        return torch.relu(torch.nn.functional.linear(v2, self.linear.weight))


# Inputs to the model
x1 = torch.randn(3, 3, requires_grad=True)
