
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0 # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise
        v3 = v1 * -0.5 # Multiply the output of the convolution by -0.5, which is equal to negative_slope in this case because we are creating a negative slope mask here
        v4 = torch.where(v2, v1, v3) # Apply where function to select elements from t1 or t3 based on the mask v2 
        return v4


# Initializing the model with negative slope 0.5. 
m = Model(-0.5)
# Inputs to the model. The input tensor is a 3 x 64 x 64 shaped image in the RGB colorspace. 
x1 = torch.randn(1, 3, 64, 64)


__output__  = m(x1)
