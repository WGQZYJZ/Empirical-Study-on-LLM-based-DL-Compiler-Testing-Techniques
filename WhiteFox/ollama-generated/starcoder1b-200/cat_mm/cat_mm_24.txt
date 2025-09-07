
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1)

    def forward(self, x1, x2):
        out1 = self.conv(x1).view(-1, x1.shape[0], x1.shape[1])
        out2 = self.conv(x2).view(-1, x2.shape[0], x2.shape[1])
        v = torch.cat([out1, out2], dim=0)
        return v


# Initializing the model
m = Model()


