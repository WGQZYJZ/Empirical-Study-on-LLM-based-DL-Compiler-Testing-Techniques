
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv1 = torch.nn.Conv2d(769, 5438, 1)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = convert_element_type(v1, torch.float) # Convert the elements of the output of the convolution by pointwise convolution into a 3-D matrix with float dtype
        v3  = torch.cumsum(v2, dim=0)  # Compute the cumulative sum along dimension `0` for each column of the 3-D matrix created with pointwise convolution to the input tensor
        v4  = self.conv1(v3)  # Apply pointwise convolution on the output of the cumsum operation in the previous step
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(20, 769, 513, 8)
