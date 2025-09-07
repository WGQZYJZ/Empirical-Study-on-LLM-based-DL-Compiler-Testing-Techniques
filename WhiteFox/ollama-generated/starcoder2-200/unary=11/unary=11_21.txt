
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1) 
        v2  = v1 + 3 # Add 3 to the output of the transposed convolution
        v3 = torch.clamp_min(v2, 0) # Clamp the output at a minimum value of 0.
        v4  = torch.clamp_max(v3, 6) # Clamp the output at a maximum value of 6.
        v5  = v4 / 6 # Divide the output by 6.
        return v5


# Initializing the model and assigning an input tensor for inference.
m = Model()
x1 = torch.randn(1, 3, 28, 28)

