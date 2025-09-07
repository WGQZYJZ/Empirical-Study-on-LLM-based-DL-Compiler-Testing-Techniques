
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1 = torch.rand(32, 50)
        self.mat2 = torch.rand(32, 50)
        self.dim = dim
 
    def forward(self, x):
         v1 = torch.addmm(x, self.mat1, self.mat2)
         v2 = torch.cat([v1], self.dim)
         return v2

 # Initializing the model
m  = Model(3).cuda()
 
# Inputs to the model
x_tensor = torch.randn(10, 50)
 
__output__  = m(x_tensor.cuda())
