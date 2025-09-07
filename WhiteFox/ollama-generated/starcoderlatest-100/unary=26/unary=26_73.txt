
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0 # Apply pointwise transposed convolution to the input tensor and create a mask where each element is True if the corresponding element in the output of the convolution is greater than 0, False otherwise
        v2 = v1 * negative_slope # Multiply the output of the transposed convolution by the negative slope
        v3 = torch.where(v1, x1, v2) # Apply the where function to select elements from the output of the convolution or the result of the multiplication based on the mask
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
