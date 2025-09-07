
class Model(torch.nn.Module):
    def __init__(self, hidden=None):
        super().__init__()
        if hidden:
            self.linear = torch.nn.Linear(10, 2)

    def forward(self, x):
        h = x[:, :3]
        o = torch.relu(self.linear(h))
        return o

# Inputs to the model
x = torch.randn(2, 4, requires_grad=True)
