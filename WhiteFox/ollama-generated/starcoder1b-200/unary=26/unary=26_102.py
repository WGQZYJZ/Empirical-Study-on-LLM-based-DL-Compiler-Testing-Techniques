
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, mask=None):
        v1 = self.conv(x1)
        v2 = torch.where(mask, v1 * negative_slope, v1) # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3 = v2 + 1  # Add 1 to the output of the where function
        v4 = v2 * 0.7071067811865476  # Multiply the output of the convolution by the negative slope
        v5 = torch.where(mask, v4 + 1, v3)  # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v5


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
mask = x1 > 0  # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
