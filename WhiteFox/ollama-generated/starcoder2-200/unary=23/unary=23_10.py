
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.tanh(v1) # Applying the hyperbolic tangent function to the output of the transposed convolution
        return v2

# Initializing the model
m = Model()

