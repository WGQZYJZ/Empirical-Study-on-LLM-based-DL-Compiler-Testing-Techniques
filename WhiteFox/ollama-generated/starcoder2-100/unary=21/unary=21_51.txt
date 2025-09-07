
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1) 
        return v2


# Initializing the model and setting the input tensor shape/dimension to a different shape from the previous one. This is necessary in order for `torch.jit.trace` to work as expected.

m = Model()

x1  = torch.randn(8, 3, 64, 57)


