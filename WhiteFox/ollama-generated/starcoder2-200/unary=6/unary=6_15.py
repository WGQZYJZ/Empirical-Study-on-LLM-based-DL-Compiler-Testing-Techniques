class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3 # Addition operation
        v4 = F.relu6(v2 / 6) # Division and ReLU6 operations
        return v4
