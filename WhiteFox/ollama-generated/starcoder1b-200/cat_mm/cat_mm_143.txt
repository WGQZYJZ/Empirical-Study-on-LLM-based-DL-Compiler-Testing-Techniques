
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(4, 8, 1)

    def forward(self, x):
        out1 = self.conv1(x)
        out2 = self.conv2(out1)
        return torch.cat([out1, out1], dim=0), torch.cat([out2, out2], dim=0)


# Initializing the model
m = Model()

