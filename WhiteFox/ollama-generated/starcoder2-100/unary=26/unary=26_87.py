
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(3, 8, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.convTranspose(x1)
        v2 = (v1 > 0).float() # Create mask
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model with a custom parameter `negative_slope`
m = Model(0.5)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # Use a randomly generated input tensor of shape (batch size=1, number of channels=3, height=64, width=64). You can also use an appropriate size for the input tensor if you have another requirement to fulfill.
