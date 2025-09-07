
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(4096, 512)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1)
        return self.fc(v2)

    def relu(self, input):
        v1 = torch.nn.ReLU()(input)
        return v1
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
