
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = torch.clamp_min(v1, min_value=-0.5) # Clamp the output of the transposed convolution to a minimum value -0.5 
        v3  = torch.clamp_max(v2, max_value=4.5)  # Clamp the output of the previous operation to a maximum value 4.5
        return v3


# Initializing model
m1 = Model()


# Inputs for the model
x1 = torch.randn(1, 3, 64, 64)
__output__= m1(x1)