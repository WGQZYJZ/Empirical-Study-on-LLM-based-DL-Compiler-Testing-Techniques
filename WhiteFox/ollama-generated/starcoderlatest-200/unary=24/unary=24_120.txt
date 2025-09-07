
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Apply pointwise convolution with kernel size 1 to the input tensor
        # And return the result of the convolution
        v2 = v1 > 0
        # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        # If the element in t1 is greater than 0 then it will be set to its corresponding value from t3 else it will remain equal to 0.
        v3 = v1 * negative_slope
        # Multiply the output of the convolution by the negative_slope 
        # And return the result of multiplying v1 with the negative slope
        v4 = torch.where(v2, v1, v3)
        # Apply the where function to select elements from v1 or v3 based on v2 (Boolean mask).
        # Return the output of t4, which will be equal to either t1 or t3
        return v4


# Initializing the model
m = Model(negative_slope=0.7)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
