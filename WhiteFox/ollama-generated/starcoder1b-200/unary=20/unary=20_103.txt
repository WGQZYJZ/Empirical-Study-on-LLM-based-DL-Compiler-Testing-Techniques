
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.ConvTranspose2d(8, 4, 2)
        self.conv_2 = torch.nn.Conv2d(4, 8, 3)
        self.activation = torch.nn.Sigmoid()

    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.activation(v1)
        v3 = self.conv_2(v2)
        return v3


# Initializing the model
m = Model()


