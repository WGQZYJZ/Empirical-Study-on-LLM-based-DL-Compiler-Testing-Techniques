
class Generator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.upsample  = torch.nn.Upsample(size=(256, 196)) # Apply upsampling followed by a non-linear activation function
        self.conv    = torch.nn.Conv2d(196, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x  = self.upsample(x1)  # Apply upsampling
        y  = self.conv(x)       # Apply pointwise convolution with kernel size 1 to the input tensor
        return y

class Discriminator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv    = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        y  = self.conv(x1)       # Apply pointwise convolution with kernel size 1 to the input tensor
        return y

class GeneratorDiscriminator(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.gd      = GeneratorDiscriminator()
        self.g_gen   = Generator()
        self.d       = Discriminator()
 
    def forward(self, x1):
        x      = self.gd(x1)  # Generate intermediate features from input tensor
        v2     = self.g_gen(x) # Apply pointwise convolution with kernel size 1 to the intermediate features
        y      = self.d(y)   # Apply pointwise convolution with kernel size 1 to the output of the generator-network
        return x, y

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.gen_discriminator  = GeneratorDiscriminator()
 
    def forward(self, x1):
        x  = self.gen_discriminator(x1) # Generate intermediate features from input tensor
        y  = self.gen_discriminator(x)  # Apply pointwise convolution with kernel size 1 to the output of generator and discriminator
        return y


# Initializing the model
m = Model()


