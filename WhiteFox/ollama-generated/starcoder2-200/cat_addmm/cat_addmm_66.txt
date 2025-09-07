
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = torch.addmm(x, self.conv.weight, self.conv2.weight) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = torch.cat([v1], dim)                                   # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4,3,64,64)
__output__  = m(x1)

