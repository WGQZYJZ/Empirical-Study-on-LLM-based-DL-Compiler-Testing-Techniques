
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1   = self.conv(x1) * 0.5 # Change 0.5 to a random constant less than 1
        v2   = self.conv(x1) + 3
        v3   = v1 / v2 # Divide the output of the convolution by another constant
        v4   = torch.erf(v3) - 78
        v5   = v4 * 0.9876
        v6_a = torch.cos(v5) * v1 + self.conv(x1) # Apply a pointwise convolution to the output of the previous convolution, apply the cosine function, and multiply it by another constant
        v6   = v6_a  - 9837204 
        return [self.conv(x1), v5]


# Initializing the model
m = Model()

 # Inputs to the model
x1    = torch.randn(1, 3, 64, 64)
 
 