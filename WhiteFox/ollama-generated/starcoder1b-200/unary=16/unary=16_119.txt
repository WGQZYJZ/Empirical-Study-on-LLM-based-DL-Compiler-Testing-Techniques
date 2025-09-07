
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64 * 4 * 4, 10)
 
    def forward(self, x):
        v = self.conv(x)
        v = v.reshape((-1, 64 * 4 * 4))
        v = self.linear(v)
        return torch.relu(v)


# Initializing the model
m = Model()

