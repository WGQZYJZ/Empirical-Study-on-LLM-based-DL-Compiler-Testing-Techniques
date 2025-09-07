
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        mask = (x1 > 0).float()  # Create a mask where each element is True if the corresponding element in x1 is greater than 0, False otherwise
        v2 = self.conv_transpose(x1) * mask # Multiply the output of the transposed convolution by the negative slope
        v3 = torch.where(mask, x1, negative_slope * mask) # Apply the where function to select elements from x1 or negative_slope based on the mask
        return v3


# Inputs to the model
x2 = torch.randn(1, 8, 10, 5)
