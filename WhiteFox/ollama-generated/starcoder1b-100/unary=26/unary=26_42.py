
class Model(nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = nn.ConvTranspose2d(3, 8, kernel_size=1)
        self.relu  = nn.LeakyReLU(negative_slope)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return self.relu(v1 * 0.5)


# Initializing the model
m = Model()


