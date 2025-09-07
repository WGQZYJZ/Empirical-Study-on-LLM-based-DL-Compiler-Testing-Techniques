
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1  = torch.randn(256)
        self.mat2  = torch.randn(256, 10)
 
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = torch.addmm(x, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = v1 + 1
        v3  = torch.cat([v2], dim) # Concatenate the result along dimension
        return v3


# Initializing the model
m  = Model(dim=0).to("cuda")


# Inputs to the model:
x1  = torch.randn(1, 3, 64, 64).to("cuda") # Input tensor for GPU
 