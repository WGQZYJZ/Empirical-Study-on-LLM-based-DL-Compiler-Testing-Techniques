
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float()  # Cast the output of the convolution to a boolean
        v3 = v1 * -0.5
        v4 = torch.where(v2, v1, v3)  # Apply where function based on mask in t2
        return v4


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
