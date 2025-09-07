
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, 3)
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 5, 2)
