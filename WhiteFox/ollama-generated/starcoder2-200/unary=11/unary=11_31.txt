
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.convt(x1) # Apply pointwise transposed convolution to the input tensor.
        v2 = v1 + 3  # Add 3 to the output of the transposed convolution.
        v3  = torch.clamp_min(v2, 0) 
        v4  = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5

m  = Model()

