
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=0)
        v1 = t1.view(t1.shape[0] * 2, -1)
        v2 = torch.relu(v1)
        return self.linear(v2)

# Inputs to the model
x1 = torch.randn(1, 3, 2)
