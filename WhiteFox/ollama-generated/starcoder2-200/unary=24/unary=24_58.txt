
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 > 0
        v3   = v1 * negative_slope # <- here, the 'negative_slope' parameter is defined at initialization of this layer, but it's not used in 'forward'
        v4   = torch.where(v2, v1, v3) # <- 'v4' is a mask where each element is True if its corresponding element is greater than 0 and False otherwise based on the output of 'v1'
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__   = m(x1)