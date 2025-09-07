
class Model(nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
    
    def forward(self, x1):
        v1  = F.conv2d(x1, 3, 8, stride=1, padding=1)
        v2  = torch.abs(v1) > 0
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, x1, v3)
        return v4


# Initializing the model
m = Model(-0.75)
