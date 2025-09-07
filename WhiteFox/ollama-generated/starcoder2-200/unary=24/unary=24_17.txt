
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3 ) #torch.where(mask, value if True, value if False)
        return v4


# Initializing the model with a specified `negative_slope` of -0.1
m = Model(-0.1)
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
