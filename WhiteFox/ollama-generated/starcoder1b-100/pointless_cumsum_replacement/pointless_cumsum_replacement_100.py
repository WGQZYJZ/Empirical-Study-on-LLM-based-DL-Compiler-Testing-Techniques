
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x).abs().sum(1).pow(2)

# Initializing the model
m = Model()


