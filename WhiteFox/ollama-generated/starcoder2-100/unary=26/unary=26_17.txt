
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = (v1 > 0).int() * -2 + (-2 < v1 < 0).int()  # create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = v1.clone() / negative_slope   # multiply the output of the transposed convolution by the negative slope 
        v4  = torch.where(v2, v1, v3)   # apply where to select elements from t1 or t3 based on mask
        return v4

# Initializing the model and setting a non-zero value for the negative_slope parameter
negative_slope = 0.75
m = Model(negative_slope)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

