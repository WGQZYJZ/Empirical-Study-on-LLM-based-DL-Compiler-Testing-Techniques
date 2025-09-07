

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = self.deconv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = v1 > 0           # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3 = v1 * negative_slope            # Multiply the output of the transposed convolution by the negative slope
        v4 = torch.where(v2, v1, v3)     # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1,8,64,64)
