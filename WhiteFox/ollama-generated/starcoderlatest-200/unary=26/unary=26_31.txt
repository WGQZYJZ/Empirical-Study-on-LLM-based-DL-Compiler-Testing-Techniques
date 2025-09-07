
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 16, stride=4, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1>0, v1, -v1 * 0.02) # Apply where to select elements from v1 or v3 based on the mask
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
