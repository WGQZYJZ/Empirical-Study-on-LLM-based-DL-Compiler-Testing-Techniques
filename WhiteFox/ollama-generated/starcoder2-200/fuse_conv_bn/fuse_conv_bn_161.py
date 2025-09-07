
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.batchnorm(x1) # Remove BatchNorm
        return conv2d(v2)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(30, 56, 80)
__output__  = m(x1)


