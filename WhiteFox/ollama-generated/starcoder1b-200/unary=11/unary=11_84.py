
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 4, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return v5


# Initializing the model
m = Model()


