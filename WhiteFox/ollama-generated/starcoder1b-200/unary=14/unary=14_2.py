
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = sigmoid(v1)
        v3 = x1 * v2
        return v3


# Initializing the model
m = Model()


