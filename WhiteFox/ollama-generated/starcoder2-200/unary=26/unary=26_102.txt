
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        mask  = v1 > 0
        v2  = negative_slope * (v1 - 0).float().clamp_(max=0.) + v1 * mask.float() # multiply element-wise
        return v2


# Initializing the model
m  = Model(negative_slope=0.5)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

