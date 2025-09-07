
class Model(torch.nn.Module):
    def __init__(self, dim: int = 2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
        self.linear1 = torch.nn.Linear(16 * dim, 8)
        self.linear2 = torch.nn.Linear(8, 4)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 + 0.5
        v3 = self.relu(v2)
        v4 = self.conv2(v3)
        v5 = v4 * v1
        v6 = v5 + v1
        return v6


# Initializing the model
m = Model()


