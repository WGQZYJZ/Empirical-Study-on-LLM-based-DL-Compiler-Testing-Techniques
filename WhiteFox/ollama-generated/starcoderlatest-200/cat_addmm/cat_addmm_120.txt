
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim)  # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 64)
