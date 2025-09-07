
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * -1  # Create a float mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = v1 * negative_slope  # Multiply the output of the convolution by the negative_slope
        return torch.where(v2, x1, v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
