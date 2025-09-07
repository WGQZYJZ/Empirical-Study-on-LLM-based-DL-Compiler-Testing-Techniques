
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        # Add the negative slope attribute to the model for later use in the forward method
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2  = (v1 > 0).float() * torch.sign(v1)
        v3 = -(v1 < -self.negative_slope).float() + \
            ((-(v1 < -self.negative_slope)).float() != 0).float() * self.negative_slope
        v4 = (torch.abs(v2) >= torch.abs(v3)).float().view(-1, 8, 64, 64)
        v5 = (v2 + v3).mul(v4)
        return v5


# Initializing the model