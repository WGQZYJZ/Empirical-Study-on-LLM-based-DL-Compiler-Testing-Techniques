
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, 4)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input tensor x1
        v2 = torch.cat([v1], dim=1)    # Concatenate the result along the first dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
x2 = torch.randn(1, 16, 32, 32)
