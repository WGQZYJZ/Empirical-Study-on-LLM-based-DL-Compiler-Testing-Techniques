
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.view(-1, 2)
        v2 = torch.relu(torch.cat([v1, x2], dim=1))
        return v2


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(4)
