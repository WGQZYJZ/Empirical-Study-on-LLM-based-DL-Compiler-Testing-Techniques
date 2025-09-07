
class Model(torch.nn.Module):
    def __init__(self, *args, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # "other" is an additional tensor passed as a keyword argument to the convolution addition operation
        return v2


# Initializing the model with different parameters
m  = Model('a' * 3, other='b' * 3)

# Inputs to the model. You can generate random tensors or just pass your own tensor.
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

