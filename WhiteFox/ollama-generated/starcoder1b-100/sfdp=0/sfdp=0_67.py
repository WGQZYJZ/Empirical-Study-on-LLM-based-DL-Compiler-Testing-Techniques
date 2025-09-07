
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.matmul(v1, x2) / (math.sqrt(v2.size(-1)) ** 0.5)
        return v3


# Initializing the model
m = Model()
