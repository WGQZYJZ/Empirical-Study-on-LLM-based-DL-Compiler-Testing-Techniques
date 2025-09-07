
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, inp=''):
        v1 = self.conv(x1) * x1  # A pointwise convolution with input tensor 'x1' is performed
        v2 = torch.mm(v1, x2)     # A matrix multiplication on two tensors 'v1' and 'x2' is performed
        return v2 + inp


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(3, 64, 64)
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(64, 3, 64, 64)
