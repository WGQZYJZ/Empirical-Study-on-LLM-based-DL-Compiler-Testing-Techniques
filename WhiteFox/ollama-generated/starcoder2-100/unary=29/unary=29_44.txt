
class Model(torch.nn.Module):
    def __init__(self, min_value = -100000., max_value  =  546792381.)
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(in_channels=3, out_channels=8, kernel_size=(1, 1), stride=(1, 1))
        
    def forward(self, x):
        v1  = self.convt(x)
        v2 = torch.clamp_min(v1, min_value=-0.5*32768) # 16-bit signed integer min = -32768
        v3  = torch.clamp_max(v2, max_value=2**14) # 16 bit signed int max = 32767
        return v3

# Initializing the model with 16-bit signed integer min and max values of `-32768` and `32767`.
m = Model(min_value=-0.5*32768, max_value=32767)

# Inputs to the model
x  = torch.randn(1, 3, 4096//8, 4096//8) # Dividing 4096 by 8 to get the width and height for 5x5 convolutions; this is the recommended size for Conv2DTranspose2d
