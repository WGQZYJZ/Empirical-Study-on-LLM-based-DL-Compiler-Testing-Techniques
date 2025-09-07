
class Model(torch.nn.Module):
    def __init__(self, minvalue=-100, maxvalue=100):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.minval = torch.full((1,), minvalue, dtype=torch.float)
        self.maxval = torch.full((1,), maxvalue, dtype=torch.float)
 
    def forward(self, x):
        v2 = self.convt(x) # Apply pointwise transposed convolution to the input tensor
        v3  = v2 - 0.5
        v4 = torch.clamp_min(v3, self.minval).clamp_max(self.maxval)
        return v4
# Initializing the model with custom min and max values
m  = Model(-1000, 987654321)


# Inputs to the model