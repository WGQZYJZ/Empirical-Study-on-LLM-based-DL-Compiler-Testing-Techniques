
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min(-0.75) # -0.75 is provided as a keyword argument 
        v3  = torch.clamp_max(v2, -0.25) # -0.25 is provided as another keyword argument
        return v3


# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(1, 8, 496, 496)
__output__  = m(x1)

