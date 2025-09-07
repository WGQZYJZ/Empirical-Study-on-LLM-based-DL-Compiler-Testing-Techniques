
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        mask_v1  = v1 > 0 # Create a boolean mask for elements in v1 that are greater than zero
        masked_v1 = torch.where(mask_v1, v1, -0.5 * v1) # Apply the where function to select from v1 or negative half of v1 based on mask_v1

        return masked_v1

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

