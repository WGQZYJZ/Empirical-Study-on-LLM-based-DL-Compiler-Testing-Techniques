
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask  = v1 > 0
        v2  = v1 * negative_slope
        v4  = torch.where(mask, v1, v2)
        return v4


# Initializing the model and set a negative slope value for LeakyReLU()
m  = Model(-0.3)
 

# Inputs to the model
x1  = torch.randn(8, 3, 64, 64)
 
# Output of the model
