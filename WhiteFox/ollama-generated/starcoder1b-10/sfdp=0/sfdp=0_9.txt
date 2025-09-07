
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)

    def forward(self, x):
        v = F.relu(self.conv1(x))
        v = F.relu(self.conv2(v))

        return torch.max(v, dim=-1)[0]

# Initializing the model
m = Model()


