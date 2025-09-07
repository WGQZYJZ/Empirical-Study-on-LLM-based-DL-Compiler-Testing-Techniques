
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = v1 * -0.5 # Multiply the output of the transposed convolution by the negative slope
        v3 = torch.where(v1, x1, v2) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
