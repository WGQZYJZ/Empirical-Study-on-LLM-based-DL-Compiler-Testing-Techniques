
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + other


# Initializing the model with a specific tensor to be added to the convolution output:
m  = Model(other)
__output__  = m(x1)
