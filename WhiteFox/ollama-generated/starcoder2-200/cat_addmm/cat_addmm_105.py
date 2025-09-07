
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat  = torch.rand(256, 784)
        self.mat1 = torch.rand(3, 200)
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1, self.mat) # 4-D matrix multiplication
        v2  = torch.cat([v1], dim=dim)            # Concatenate the result along dimension 3 
        return v2


# Initializing the model
m  = Model(3).cuda() 

# Inputs to the model (GPU)
x1 = torch.randn(4, 784, 600, 500).cuda() # 4-D input tensor of 8-bit integers

# Outputs from the model (GPU)
