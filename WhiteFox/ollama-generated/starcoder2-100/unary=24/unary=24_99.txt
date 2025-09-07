
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        mask  = v1 > 0 # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2  = torch.where(mask, v1, -v1*negative_slope) # Apply the where function to select elements from t1 or t3 based on the mask
        return v2


# Initializing the model with negative slope of `0.2`
m  = Model(negative_slope=0.2)

# Input tensor for the model
x1  = torch.randn(4, 3, 64, 64)
__output__  = m(x1)

