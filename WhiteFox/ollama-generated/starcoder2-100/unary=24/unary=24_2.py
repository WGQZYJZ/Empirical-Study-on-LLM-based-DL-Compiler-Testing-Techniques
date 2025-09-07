
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1596724938014528):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
        v1    = self.conv(x1)
        v2    = (v1 > 0).type_as(v1) # Convert the boolean mask to floating-point type based on v1's type
        v3    = negative_slope * (-v1 if v2 == 0 else torch.zeros_like(v1)) # Use a multiplication and conditional selection to implement the negative slope activation function with a mask to handle zeros in v1
        v4,  = torch.where(v2, v1, v3) # Apply the where function on the mask to choose values from v1 or v3 based on whether there is non-zero value in v1 
        return v4

# Initializing the model with a fixed negative_slope value of `0.159672`
m  = Model(negative_slope=0.159672) 

# Inputs to the model using a fixed negative_slope value of `0.159672`.
x1 = torch.randn(1, 3, 64, 64)
__output__    = m(x1)

