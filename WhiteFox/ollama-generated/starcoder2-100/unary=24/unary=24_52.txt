
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
    
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        mask  = torch.nn.functional.threshold(v1, 0., threshold=self.negative_slope) 
        v2  = torch.where(mask, v1, -v1*self.negative_slope)
        return v2

# Initializing the model with negative_slope value of 0.5
m = Model(negative_slope=0.5)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # An input tensor for the model

 __output__  = m(x1)
 
