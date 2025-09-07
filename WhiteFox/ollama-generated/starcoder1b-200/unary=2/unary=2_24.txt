
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 4) # The output of the convolution is squared
        v4 = torch.mul(v1, v3) # The output of the multiplication is cubed
        v5 = torch.erf(v4)
        v6 = torch.mul(v5, 2)
        v7 = torch.tanh(v6) + 1
        v8 = v2 * v7
        return v8


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
