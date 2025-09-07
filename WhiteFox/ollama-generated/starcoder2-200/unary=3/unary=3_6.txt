
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + F.pad(v1, [0, 0, 1, 1])
        return v2


# Initializing the model
m = Model()
