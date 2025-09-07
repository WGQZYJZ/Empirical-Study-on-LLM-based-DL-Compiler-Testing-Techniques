

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3 = v1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476

        # Add code here to replace the line above with a custom torch function:
        return v3

