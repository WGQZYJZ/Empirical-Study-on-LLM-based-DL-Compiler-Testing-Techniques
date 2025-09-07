
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(32, 64) 
        self.mat2 = torch.randn(64, 32) 
        self.input = torch.randn(1024, 8)
 
    def forward(self, x1):
        v1 = torch.addmm(self.input, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim=1) # Concatenate the result along a specified dimension 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 1024)
