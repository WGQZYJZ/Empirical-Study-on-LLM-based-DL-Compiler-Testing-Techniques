
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(4, 16)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.addmm(v1, x, x.transpose(-1, -2))
        v3 = v2 + v2  # Add square of matrix twice to obtain a third matrix (third layer)
        v4 = v3 + v3  # Add square of matrix twice again to obtain the fourth matrix
        v5 = torch.cat([v4, v4], dim=1)
        v6 = self.fc1(v5)
        return v6


# Initializing the model
m = Model()


