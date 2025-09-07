
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v2, 3.0) * 2.0
        v4 = torch.pow(v2, 2.0) * v3
        v5 = v4 + 1
        v6 = v5 * 1.79789e+3 # Multiply the output of the addition by 1.79789e+3
        v7 = torch.tanh(v6) + 1
        v8 = v7 * (0.9999239454235818 + 1.2109167348797513*torch.exp(-0.7353904563639628)) # Multiply the output of the multiplication by (0.9999239454235818 + 1.2109167348797513*exp(-.7353904563639628))
        return v8


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 16, 16)
