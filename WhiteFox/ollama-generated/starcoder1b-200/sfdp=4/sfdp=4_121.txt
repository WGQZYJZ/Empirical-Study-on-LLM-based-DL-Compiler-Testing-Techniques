
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.fc1   = torch.nn.Linear(8 * 4 * 4, 128)
        self.fc2   = torch.nn.Linear(128, 1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5

        k1 = self.conv2(v6).transpose(-2, -1)
        k2 = torch.tanh(self.fc1(k1))
        k3 = torch.relu(self.fc2(k2))
        return k3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 480, 640)
