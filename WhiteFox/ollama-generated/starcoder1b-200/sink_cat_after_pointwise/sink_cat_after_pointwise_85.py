
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.relu(torch.cat([v1, x1], dim=1))
        return torch.sigmoid(self.linear(v2))


# Initializing the model
m = Model()


