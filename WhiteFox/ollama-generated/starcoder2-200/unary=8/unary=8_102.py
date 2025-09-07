
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)

    def forward(self, x1):
        v0 = self.convT(x1)
        v1 = v0 + 3 # Add 3 to the transposed convolution output (v1) 
        v2 = torch.clamp(v1, min=0) # Clamp the addition operation by the maximum value of 6
        v3 = torch.clamp(v2, max=6) # Clamp the previous clamp operation by the maximum value of 6 
        return v3
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)


