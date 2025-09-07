
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2    
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
__output__  = m(x1)

- `torch.nn.Conv2d`: Applies a convolution over an input signal composed of several input planes.
- `torch.sigmoid`: Applies the sigmoid function elementwise.
- `torch.erf`: Calculates the error function of the elements of each batch, element by element.

