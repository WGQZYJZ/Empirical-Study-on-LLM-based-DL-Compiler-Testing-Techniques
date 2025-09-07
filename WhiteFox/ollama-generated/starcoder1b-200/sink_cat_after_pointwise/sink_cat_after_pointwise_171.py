
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, kernel_size=(1, 1), stride=(1, 1))

    def forward(self, x1):
        return self.conv(x1)


# Initializing the model
m = Model()


# Inputs to the model
inputs = torch.randn(1, 3, 4, 4)
