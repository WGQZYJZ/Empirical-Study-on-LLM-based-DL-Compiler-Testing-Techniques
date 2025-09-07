
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, other=0.5):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v4  = v1 + other
        return v4


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other_tensor  = torch.zeros([1], dtype=torch.float32) # Initialize other tensor that is passed as a keyword argument
