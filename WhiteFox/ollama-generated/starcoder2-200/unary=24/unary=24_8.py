
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.neg_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = (v1 > 0).float() # Generate a boolean mask by comparing the output of the convolution to zero
        v3 = v1 * self.neg_slope # Multiply the output of the convolution by the negative slope, assuming that the negative slope is positive
        v4 = torch.where(v2, v1, v3)  # Use the where function with the mask from before to choose elements in either v1 or v3 based on the mask
        return v4


# Initializing the model