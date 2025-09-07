
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.sign(v1) > 0   # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = v1 * self.negative_slope # Multiply the output of the convolution by the negative_slope
        v4  = torch.where(v2, v1, v3)  # Apply the where function to select elements from v1 or t3 based on the mask v2 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)

# Running forward pass of the model with randomly generated inputs
__output__  = m(x1)