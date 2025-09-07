
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Add constant 3 to output of the convolution operation
        v4  = torch.clamp_min(v2, 0).clamp_max(6) # Clamp the result of addition to a minimum value of 0 and a maximum value of 6
        v5  = v1 * v4 # Multiply output of the convolution by clamped result 
        v7  = v5 / 6 # Divide result of multiplication operation by constant 6.
        return v7

# Initializing the model
m = Model()

