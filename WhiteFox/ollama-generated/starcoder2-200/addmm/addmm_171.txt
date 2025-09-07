
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Input tensor for matrix multiplication operations
inp = torch.randn(8*8) # The tensor of which the size is 512 (64 * 8). This is used to add another tensor as a keyword argument.

# Initializing the model and running it with inputs x1, inp
