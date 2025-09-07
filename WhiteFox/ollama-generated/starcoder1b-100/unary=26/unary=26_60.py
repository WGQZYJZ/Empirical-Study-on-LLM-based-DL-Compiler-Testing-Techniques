
class Model(nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = nn.ConvTranspose2d(8, 16, 1, stride=2, padding=0)
 
    def forward(self, x):
        v1 = F.leaky_relu(self.conv(x), negative_slope)  # Apply the Leaky ReLU operation to the output of the convolution
        return self.conv(v1)


# Initializing the model
m = Model()


