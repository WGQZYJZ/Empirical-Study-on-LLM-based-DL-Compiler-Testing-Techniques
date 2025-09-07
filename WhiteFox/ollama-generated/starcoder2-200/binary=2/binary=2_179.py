
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other  # subtracting 'other' from the output of the convolution
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = ...  # some tensor or scalar with shape [1, 8, 64, 64] for example, 0.5, or -0.707...
