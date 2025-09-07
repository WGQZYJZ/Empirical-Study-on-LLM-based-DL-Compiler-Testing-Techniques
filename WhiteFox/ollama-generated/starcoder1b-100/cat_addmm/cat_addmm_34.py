
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.fc1 = torch.nn.Linear(4096, 512)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = v1 + x2
        v3 = v2 * 2
        v4 = torch.sigmoid(v3)
        return v4


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(3, 512)
