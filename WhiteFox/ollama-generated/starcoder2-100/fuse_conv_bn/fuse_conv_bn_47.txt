
class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.linear(x1, self.linear.weight) # Apply linear transformation to the permuted tensor.
        return v2

class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x3):
        v4  = torch.nn.functional.conv2d(x3, self.conv.weight) # Apply convolution to the permuted tensor.
        return v4

# Initializing the model