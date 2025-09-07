
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(8, 4, 7, stride=(2, 2), padding=(1, 1))

    def forward(self, x):
        v1 = self.conv1(x)
        v3 = v1 * 0.5
        v4 = torch.sigmoid(v3)
        v6 = v4 + 1
        return v6

# Initializing the model
m = Model()

