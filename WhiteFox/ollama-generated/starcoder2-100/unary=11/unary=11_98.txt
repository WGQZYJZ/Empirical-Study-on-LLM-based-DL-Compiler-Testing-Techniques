
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 10, kernel_size=5)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0, max=6) / 6 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 3, 8, 7) # Generate a random 4D tensor with size [4 x 3 x 8 x 7] as an input.

__output__  = m(x1)
