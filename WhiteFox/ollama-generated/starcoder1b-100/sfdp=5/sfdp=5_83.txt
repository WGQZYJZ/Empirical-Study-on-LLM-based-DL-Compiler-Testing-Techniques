
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(16 * 4 * 4, num_classes)

    def forward(self, x):
        v = self.conv(x)
        h = v.view(-1, 16 * 4 * 4)
        out = self.fc(h).flatten()
        return out


# Initializing the model
m = Model()

