
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, kernel_size=3)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        out = torch.cat([self.relu(x), self.conv1(x)], dim=1)
        return out

# Initializing the model
m = Model()

