
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.convT(x1) 
        v2 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the transposed convolution
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
