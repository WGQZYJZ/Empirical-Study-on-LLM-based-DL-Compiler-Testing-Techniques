# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = x1  # Assign a new copy of `x1` to another name in the closure scope
        t2 = self.conv(t1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        t3 = t1 * 0.5  # Multiply the output of the convolution by 0.5
        t4 = t1 * 0.7071067811865476  # Multiply the output of the convolution by 0.7071067811865476
        t5 = torch.erf(t3)  # Apply the error function to the output of the convolution
        t6 = t4 + 1  # Add 1 to the output of the error function
        t7 = t2 * t6  # Multiply the output of the convolution by the output of the error function
        return t7


