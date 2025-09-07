
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = -v2 * 2 # Use a negative value to scale the convolution
        v4 = torch.where(v2, v1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model
m = Model()


