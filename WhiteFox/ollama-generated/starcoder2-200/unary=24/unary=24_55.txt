
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1) # Apply pointwise convolution with kernel size 1 to the input tensor
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1) # Convolution with negative slope
        mask = torch.tensor([v1 >0])
        mask = mask.float() # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        
        v2 = v1 * self.negative_slope
        v3 = torch.where(mask, v1, v2) # Apply the where function to select elements from t1 or t2 based on the mask
        return v3


# Initializing the model and generating input tensors. 
m = Model()
 
x1 = torch.randn(1,3,64,64)
