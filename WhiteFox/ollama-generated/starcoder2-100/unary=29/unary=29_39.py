
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, -0.5) # clamp the output of the transposed convolution to a minimum value `-0.5` (negative infty)
        v3 = torch.clamp_max(v2, 0.9867497570787335) # clamp the output of the previous operation to a maximum value `0.9867497570787335` (positive infty)
        return v3


# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(1, 8, 12, 12)
