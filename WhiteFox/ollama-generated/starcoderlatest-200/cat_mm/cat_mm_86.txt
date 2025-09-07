
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = torch.cat([v1, v1, ..., v1]) # Concatenate the output of convolution by adding a constant to each element
        return v2


# Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
