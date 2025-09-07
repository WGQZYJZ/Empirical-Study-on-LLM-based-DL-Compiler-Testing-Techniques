
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1) # Hyperbolic tangent activation function on the convolution output
        return v2


# Initializing model
m  = Model()
__output__  = m(torch.randn(1, 3, 64, 64)) # Generating an input to the model that meets the specified requirements