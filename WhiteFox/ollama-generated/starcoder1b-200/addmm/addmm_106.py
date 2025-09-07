
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, inp):
        v1 = self.conv1(x1)
        return v1 + inp


# Initializing the model
m = Model()

