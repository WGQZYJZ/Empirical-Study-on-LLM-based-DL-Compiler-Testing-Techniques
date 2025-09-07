
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat = torch.randn(32)
        self.mat1  = self.mat.reshape(8,4)
        self.mat2  = self.mat.reshape(4,8).transpose()
 
    def forward(self, x):
        v1  = torch.addmm(x, self.mat1, self.mat2) # perform a matrix multiplication of mat1 and mat2 
        v2 = torch.cat([v1], dim=dim)# concatenate the result along a specified dimension
        return v2


# Initializing the model
m  = Model()


Inputs to the model