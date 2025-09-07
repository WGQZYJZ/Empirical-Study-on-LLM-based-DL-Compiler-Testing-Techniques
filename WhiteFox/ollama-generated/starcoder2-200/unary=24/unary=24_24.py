
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask = (v1 > 0).float() 
        v2  = v1 * negative_slope * mask
        v4  = torch.where(mask, v1, v2) # Apply the where function to select elements from t1 or t3 based on the mask
        return v4

# Initializing the model
m = Model(negative_slope=0.5)

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

