
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv_transpose  = torch.nn.ConvTranspose2d(32, 64, 1)
        self.leaky_relu  = torch.nn.LeakyReLU()
 
    def forward(self, x):
        v1  = self.conv_transpose(x)
        v2  = (v1 > 0).type(torch.float32) * negative_slope
        v3  = v1 + v2 # Elementwise add
        return self.leaky_relu(v3)


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(5, 32, 640, 780)
__output__  = m(x)

