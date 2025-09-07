
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.relu    = torch.nn.ReLU()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)
        v2 = self.relu(v1.view(-1, 8))
        return v2


# Inputs to the model
x1 = torch.randn(2, 4, 2)
