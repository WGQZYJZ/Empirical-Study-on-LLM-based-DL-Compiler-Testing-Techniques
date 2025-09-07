

# Model
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).clamp_(-0.5, 0.5) # Clamp the output of the convolution to [-0.5, 0.5] range
        v2 = -v1 * negative_slope
        v3 = torch.where(v2 > 0, v1, v2) # Apply where function to select elements from v1 or the result of the multiplication based on the mask v2>0
        return v3


# Initializing the model
m = Model(negative_slope=0.75)

