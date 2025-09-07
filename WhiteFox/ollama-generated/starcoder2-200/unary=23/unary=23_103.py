
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.deconv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1=self.deconv(x1) # Applying pointwise transposed convolution to the input tensor
        v2 = torch.tanh(v1) # Apply hyperbolic tangent function
        return v2


# Initializing model
m  = Model()

# Inputs to the model
x1=torch.randn(1,3,64,64)

