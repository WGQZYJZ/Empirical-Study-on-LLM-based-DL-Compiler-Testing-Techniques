
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, -v1 * 0.5) # Mask v2 by where t1 > 0 and multiply the output of the convolution by -0.5
        v3 = torch.abs(v1) * v2 # Add the absolute value of the magnitude of each element in t1 to the mask t2
        return v3


# Initializing the model
m = Model()

