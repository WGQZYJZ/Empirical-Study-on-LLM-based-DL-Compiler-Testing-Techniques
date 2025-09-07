
class Model(nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv_transpose = nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x):
        v = self.conv_transpose(x) > 0
        return (1-self.negative_slope)*v + self.negative_slope*v

# Initializing the model
m = Model()


