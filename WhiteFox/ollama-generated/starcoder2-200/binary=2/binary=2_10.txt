
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1)

    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = v1 - other 
        return v2


# Initializing the model
m  = Model()
other = torch.zeros([3,8], dtype=torch.float64) # Initialize 'other' to be a tensor of shape (3,8) with values of type float64.

# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)

__output__  = m(x1)

