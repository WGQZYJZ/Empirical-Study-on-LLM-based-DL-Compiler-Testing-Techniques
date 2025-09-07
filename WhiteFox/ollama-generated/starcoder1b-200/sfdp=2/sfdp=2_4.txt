
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)

    def forward(self, x):
        v = self.conv1(x)
        k = self.conv2(v)
        s = torch.softmax(k, dim=-1)
        return torch.matmul(s, v)

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
