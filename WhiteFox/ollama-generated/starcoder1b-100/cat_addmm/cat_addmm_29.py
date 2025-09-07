
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(512, 64)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.7071067811865476
        v3 = v1  + 1
        v4 = torch.tanh(v3)
        v5 = v2 * v4
        return v5


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 64, 512, 10)
