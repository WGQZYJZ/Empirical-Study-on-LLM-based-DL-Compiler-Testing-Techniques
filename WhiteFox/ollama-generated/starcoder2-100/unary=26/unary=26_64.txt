
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask_v2  = v1 > 0 
        v3  = -1 # negative slope to apply to the output of the transposed convolution
        v4  = torch.where(mask_v2, v1, v3)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model