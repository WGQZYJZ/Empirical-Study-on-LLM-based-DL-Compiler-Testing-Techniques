
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
    def forward(self, x0): 
        v1  = self.conv(x0).sum()  # Add the output of a pointwise convolution
        v5  = torch.relu(v1 + other)
        return v3


# Initializing the model
m  = Model()
other  = 8  # The constant to be subtracted from the output of the linear transformation (in this example, 'other' is a constant of 8)
x0  = torch.randn(1, 3, 64, 64)
