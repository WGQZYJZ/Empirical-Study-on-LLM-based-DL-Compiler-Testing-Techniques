
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.l = torch.nn.Linear(64 * 64 * 8, 1024)

    def forward(self, x):
        v1 = self.conv(x)
        t1 = self.l(v1.view(-1, -1))
        v2 = torch.sigmoid(t1)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3, 32, 64, 64)
