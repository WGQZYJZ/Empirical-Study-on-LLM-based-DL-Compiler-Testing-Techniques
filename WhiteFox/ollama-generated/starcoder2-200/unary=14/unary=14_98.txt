
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * self.relu(v1) # A typical GLU operation: multiply the output of the transposed convolution by the output of the relu function
        
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
