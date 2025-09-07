
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 > 0
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4

# Initializing the model
m  = Model()

