
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        negative_slope = 0.5 * torch.ones([8, 32, 64, 64], dtype=torch.int) # Set the negative slope to 0.5 for each channel 
        v3 = v1 * negative_slope
        v4 = torch.where(mask == True, v1, v3)
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
