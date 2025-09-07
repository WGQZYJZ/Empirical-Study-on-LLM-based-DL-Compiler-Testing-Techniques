
class UpsampleConv2d(nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.conv = nn.Sequential(
            Conv2d(dim, dim, 3),  # Apply a convolutional layer to the input tensor
            BatchNorm2d(dim),
            nn.ReLU(),
            nn.Upsample((2, 2)),  # Apply an upsampling operation (2x2 in this case)
        )
 
    def forward(self, x):
        return self.conv(x)


class Generator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder()

    def forward(self, x):
        return self.encoder(x)  # Apply the encoder to input x

    def inference(self, z):
        with torch.no_grad():
            x = self.encoder.inference(z)  # Get the representation of the random noise
            return UpsampleConv2d(self.encoder.dim)(x)


# Initializing the generator
g = Generator()


