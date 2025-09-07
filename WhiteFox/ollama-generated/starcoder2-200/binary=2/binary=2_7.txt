
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1) - 0.5 # Subtract 'other' from the output of the convolution (the output of the convolution is 64x64 in size here.)
        return v1


# Initializing the model
m = Model()
