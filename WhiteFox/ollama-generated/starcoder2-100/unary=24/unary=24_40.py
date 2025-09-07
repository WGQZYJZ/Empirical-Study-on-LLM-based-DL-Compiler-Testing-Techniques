
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).int() 
        v4 = torch.where(mask == True, v1, negative_slope * v1) # Apply the where function to select elements from t3 or the result of the multiplication based on the mask.
        return v4

# Initializing the model