
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 16, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        negative_slope = torch.tensor(-1).unsqueeze(1).unsqueeze(1).unsqueeze(1) # A scalar tensor representing a single-element constant
        t2 = v1 > 0  # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        t3 = v1 * negative_slope # Multiply the output of the convolution by the negative slope
        v4 = torch.where(t2, v1, t3) # Apply the where function to select elements from v1 or t3 based on the mask t2
        return v4
