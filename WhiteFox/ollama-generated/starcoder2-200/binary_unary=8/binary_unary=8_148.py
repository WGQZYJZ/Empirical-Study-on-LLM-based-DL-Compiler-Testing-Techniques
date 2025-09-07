
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor.
        v2  = v1 + other_tensor # Add another tensor to the output of the convolution.
        v3  = torch.relu(v2)   # Apply the ReLU activation function to the result
        return v3


# Initializing and testing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
other_tensor = 50*torch.ones(2**9, 8, 7, 7) # This is an extra tensor which is added to conv output

__output__= m(x1).sum()

