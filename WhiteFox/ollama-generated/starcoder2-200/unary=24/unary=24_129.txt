
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0 # Create boolean mask based on output of the conv layer.
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model(negative_slope=0.5)
 
# Inputs to the model
x  = torch.randn(1,3,64,64)
