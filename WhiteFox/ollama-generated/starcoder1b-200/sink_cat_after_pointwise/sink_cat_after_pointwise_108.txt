
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = torch.relu(torch.cat([x1, x1], dim=0))
        return v2


# Inputs to the model
x1 = torch.randn(3, 2)
