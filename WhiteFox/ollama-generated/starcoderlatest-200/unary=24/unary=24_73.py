
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * negative_slope # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise 
        v3 = v1 * v2 # Multiply the output of the convolution by the result of the multiplication based on the boolean mask
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
