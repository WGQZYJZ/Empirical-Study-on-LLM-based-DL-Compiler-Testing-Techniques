
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask  = (v1 > 0)  # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = torch.where(mask, x1, -self.negative_slope * v1)  # Apply the where function to select elements from v1 or negative slope based on the mask
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
