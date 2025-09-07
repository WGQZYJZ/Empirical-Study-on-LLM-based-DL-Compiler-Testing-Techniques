
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # t1 is the mask for whether each element in x1 is larger than 0 or not
        t1 = torch.where(v1 > 0, v1, -v1)
        v2 = t1 * self.negative_slope  # Multiply the output of the convolution by the negative_slope
        v3 = t1 * (-self.negative_slope)  # Multiply the output of the convolution by the negative_slope
        v4 = torch.where(t1 > 0, x1, (v2 + v3))  # Apply the where function to select elements from the output of the convolution or the result of the multiplication based on the mask t1
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
