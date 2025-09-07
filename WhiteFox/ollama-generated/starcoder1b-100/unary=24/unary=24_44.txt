
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x).view(x.shape[0], -1).mm(torch.tensor([negative_slope]))


# Initializing the model
m = Model()


