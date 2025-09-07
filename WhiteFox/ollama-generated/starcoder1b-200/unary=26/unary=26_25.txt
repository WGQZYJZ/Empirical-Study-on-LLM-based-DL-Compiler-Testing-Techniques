
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x):
        v = self.conv_transpose(self.conv(x))
        return v


# Initializing the model
m = Model()


