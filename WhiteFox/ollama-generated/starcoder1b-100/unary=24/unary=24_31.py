
class Model(nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = x1 > 0
        v3 = torch.where(v2, x1 * self.negative_slope, x1)  # Apply the where function to select elements from t1 or t3 based on the mask v2
        # Multiply the output of the convolution by the negative_slope
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
