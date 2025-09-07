
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1) 
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t2 = v1 > 0 # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        t3 = v1 * self.negative_slope # Multiply the output of the transposed convolution by the negative slope
        t4 = torch.where(t2, v1, t3) # Apply the where function to select elements from v1 or the result of multiplication based on the mask
        return t4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
