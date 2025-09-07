
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v4  = v1 * negative_slope 
        v5  = torch.where(v2, v3, t4) 
        return v5

m = Model() # Create an instance of the model with a negative slope of 0.5


# Initializing the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

# Generate inputs for the model: a random tensor and a constant value (negative_slope)
negative_slope  = 0.5
t2  = t1  * negative_slope # Multiply the output of the convolution by the negative slope
t4  = torch.where(v2, v3, t4) # Apply the where function to select elements from t1 or t3 based on the mask t2

