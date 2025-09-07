
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(v1.shape[0] * 2, -1)
        v3 = torch.relu(v2)
        return self.linear(v3)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 1)
x2 = torch.randn(1, 3, 1)
