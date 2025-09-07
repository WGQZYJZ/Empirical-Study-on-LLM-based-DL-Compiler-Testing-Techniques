
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.158):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4

# Initializing the model
m  = Model(negative_slope=0.158)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

