
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = torch.where(v2, v1, -self.negative_slope * v1) # Create a mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise, then multiply the output of the transposed convolution by negative_slope
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x2  = torch.randn(1, 8, 64, 64)
__output__  = m(x2)

