
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1.permute(0, 2, 1), x1], dim=2)
        v2 = torch.relu(v1.view(v1.size()[0] * v1.size()[1], -1))
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(3, 2, 2)
