
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)

        mask = (v1 > 0).float()
        # - 1 is the negative slope used to prevent numerical issues that may arise from rounding to zero in float
        v3 = torch.where(mask == 1., v1, (-1 * mask))
        
        return v3


# Initializing the model
negative_slope = 0.5
m = Model(negative_slope)


 # Inputs to the model
    x1 = torch.randn(1, 3, 64, 64)

    