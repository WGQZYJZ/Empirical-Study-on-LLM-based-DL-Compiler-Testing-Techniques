
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v0 = self.convT(x) # Apply pointwise transposed convolution to the input tensor. The size of this output should match the input tensors' size.
        v1 = torch.tanh(v0) # Apply the hyperbolic tangent function to the output of the transposed convolution.
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(1, 8, 64, 64)
