
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask_v1 = (v1 > 0).to(torch.bool) 
        slope_v1 = v1 * negative_slope
        masked_v1  = torch.where(mask_v1, v1, slope_v1 )
        return masked_v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
