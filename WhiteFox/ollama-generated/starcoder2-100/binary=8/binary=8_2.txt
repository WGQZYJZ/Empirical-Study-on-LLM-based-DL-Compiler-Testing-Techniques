

class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        self.conv1d = torch.nn.Conv2d(3, 8, 1)
        if other is not None and isinstance(other, torch.nn.Conv2d):
            self.conv2d  = other
        else:
            self.conv2d  = torch.nn.Conv2d(3, 9, 4)
 
    def forward(self, x1):
        v1 = self.conv1d(x1) + self.conv2d(x1) # Add the output of two pointwise convolutions with different kernels to each other
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 64, 64)

# Pass the second argument in order for the 2nd convolution to be used instead of the default one provided in the initializer
m(x1).size(), m(x1, self.conv1d(torch.zeros_like(x1)) * other=self.conv1d(torch.zeros_like(x1))).size()
