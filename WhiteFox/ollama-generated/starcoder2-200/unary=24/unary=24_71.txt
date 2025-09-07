
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask = (v1 > 0).int() # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3  = -2 * negative_slope * ((-mask + 1)/2) 
        v4  = torch.where(mask == 1, v1, v3 ) # Apply the where function to select elements from v1 or v3 based on the mask
        
        return v4


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(256, 3, 80, 79)
__output__  = m(x1)

