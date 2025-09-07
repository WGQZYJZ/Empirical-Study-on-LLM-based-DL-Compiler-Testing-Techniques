
class Model(torch.nn.Module):
    def __init__(self, inplace=True):
        super().__init__()
        self.inplace = inplace
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, x1], dim=1)
        v3 = torch.relu(torch.relu(self.linear(v2)))
        return (x1 - v3).view_as(x1)


# Initializing the model
m = Model()
