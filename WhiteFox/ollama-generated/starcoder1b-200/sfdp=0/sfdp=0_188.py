
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale = 100

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * self.scale
        v3 = torch.matmul(v2, v2.transpose(-2, -1)) / math.sqrt(self.scale)
        output = torch.matmul(v3, v1) + 1
        return output


# Initializing the model
m = Model()


