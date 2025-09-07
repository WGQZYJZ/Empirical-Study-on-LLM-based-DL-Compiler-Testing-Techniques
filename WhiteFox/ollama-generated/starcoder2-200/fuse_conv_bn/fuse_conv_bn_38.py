
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 50, kernel_size=1)

    def forward(self, x):
        v1  = torch.nn.functional.batchnorm(torch.nn.functional.conv2d(x), self.conv.weight, self.conv.bias) # Fused into a single convolution layer here!
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4096*5, 3)
__output__  = m(x)


