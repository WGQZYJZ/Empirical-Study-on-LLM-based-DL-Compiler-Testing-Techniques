
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1) # pointwise transposed convolution
        v2  = torch.tanh(v1)  # hyperbolic tangent function of the output
        return v2


# Initializing the model and setting optimizer