
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = self.conv1(x1)  # Apply pointwise convolution with kernel size 3 to the input tensor
        v2 = torch.relu(v1 + other)  # Add another tensor (specified by the keyword argument "other") to the output of the convolution
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1, other  = torch.randn(3), 0
__output__  = m(x1)