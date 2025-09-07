
class Model(nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        m1 = (v1 > 0).float()  # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        m2 = ((m1 * negative_slope)).float()  # Multiply the output of the transposed convolution by the negative slope
        v4 = torch.where(m2, x1, m1)  # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
