
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v = torch.nn.functional.conv2d(x, weight) # Convolution followed by batch normalization
        return v * self.bn(v) # Batch normalization followed by multiplication


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 4, 30, 20)
