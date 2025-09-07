
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        mask = v1 > 0 # Create boolean mask for each element in v1; set to True if greater than 0 and False otherwise
        v2 = torch.where(mask, v1, -v1*negative_slope) # Select elements from v1 or -v1*negative_slope based on the mask 'mask' 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__   = m(x1)

