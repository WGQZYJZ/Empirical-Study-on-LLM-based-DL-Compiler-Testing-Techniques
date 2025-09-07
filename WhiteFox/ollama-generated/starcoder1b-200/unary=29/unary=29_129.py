
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, **kwargs):
        return self.conv(x1, x2, **kwargs)


# Initializing the model
m = Model()


