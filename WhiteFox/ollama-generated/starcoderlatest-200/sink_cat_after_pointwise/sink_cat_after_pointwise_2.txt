
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = v1.view(2, -1)
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(4, 2, 2)
