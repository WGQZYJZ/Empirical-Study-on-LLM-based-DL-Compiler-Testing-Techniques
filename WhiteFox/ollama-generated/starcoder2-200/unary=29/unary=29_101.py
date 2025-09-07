
class Model(torch.nn.Module):
    def __init__(self, minval=-0.75, maxval=21348.98):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(in_channels=24, out_channels=6, 
                                              kernel_size=(3, 3), stride=3, padding=0)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp(v1, minval=-0.75, maxval=21348.98)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(2, 6, 31, 31)

# Output from the model
__output__  = m(x1)

