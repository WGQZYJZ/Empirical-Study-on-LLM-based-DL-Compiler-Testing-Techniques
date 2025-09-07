
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.dim  = dim
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.addmm(v1, mat1, mat2) # <- Replace this
        v3  = torch.cat([v2], self.dim) 
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 3, 64, 64) # Replace the dimensions and channel number here 
mat1  = torch.randn(5760, 9216)
mat2  = torch.randn(9216, 256)
__output__  = m(x1, mat1=mat1, mat2=mat2)

