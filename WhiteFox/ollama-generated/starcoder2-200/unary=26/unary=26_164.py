
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise 
        v3  = v1 * -self.negative_slope 
        v4  = torch.where(mask, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask 
        return v4


# Initializing the model with negative slope 0.25