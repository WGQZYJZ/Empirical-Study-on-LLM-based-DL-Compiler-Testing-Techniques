
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).to(torch.float32) # Boolean mask
        v4  = v1 * -self.negative_slope
        v5  = torch.where(v2, v1, v4)
        return v5

# Initializing the model
m  = Model(0.8)
 
# Inputs to the model
x1 = torch.randn(1,3,64,64)
__output__  = m(x1)

