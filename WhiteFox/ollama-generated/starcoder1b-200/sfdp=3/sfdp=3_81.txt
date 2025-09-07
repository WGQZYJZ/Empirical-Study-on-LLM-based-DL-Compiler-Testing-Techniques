
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(8, 5)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.fc1(v1)
        return output


# Inputs to the model
q1  = torch.randn(1, 3, 64, 64)
k1  = torch.randn(1, 8, 64, 64)
v1  = torch.randn(1, 5, 64, 64)
