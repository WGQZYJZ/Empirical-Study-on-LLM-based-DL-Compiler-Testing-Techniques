
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        return v2


# Initializing the model with the input tensor for the second convolution layer
m  = Model(torch.zeros_like(x1))
__output__  = m(x1)

