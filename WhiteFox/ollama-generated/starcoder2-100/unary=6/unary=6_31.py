
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x):
        v0 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v1 = v0 + 3  # Add 3 to the output of the convolution
        v2 = torch.clamp_min(v1, 0)  # Clamp the output of the addition operation to a minimum of 0
        v3 = torch.clamp_max(v2, 6)  # Clamp the output of the previous operation to a maximum of 6
        v4 = v0 * v3   # Multiply the output of the convolution by the clamped result
        v5 = v4 / 6    # Divide the output of the multiplication operation by 6
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(2,3,64,64)
