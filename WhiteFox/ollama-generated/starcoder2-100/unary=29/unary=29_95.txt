
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.clamp_min(v1, min=-0.5) # Add minimum value -0.5 to the output of the transposed convolution operation 
        v3  = torch.clamp_max(v2, max=0.875) # Clamp maximum value with 0.875
        return v3


# Initializing the model
m  = Model()

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)

__output__  = m(x1)

