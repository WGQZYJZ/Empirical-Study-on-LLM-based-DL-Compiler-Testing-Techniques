
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = torch.tanh(v1) # Add hyperbolic tangent function here
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model 
x1 = torch.randn(3, 8, 4096, 4096)
