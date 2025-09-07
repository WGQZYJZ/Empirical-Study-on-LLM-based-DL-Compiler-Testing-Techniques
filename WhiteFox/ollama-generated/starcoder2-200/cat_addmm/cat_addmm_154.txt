
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None, input=None):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if mat1 is not None:
            self.mat1 = mat1
        else:
            self.mat1 = torch.rand_like(self.conv.weight)
 
        if mat2 is not None:
            self.mat2 = mat2
        else:
            self.mat2 = torch.rand_like(self.conv.weight)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v1  = torch.addmm(v1, self.mat1, self.mat2)
        v1  = torch.cat([v1], dim)
        return v1

# Initializing the model with inputs as mat1 and mat2 (or random matrices generated at initialization).
m  = Model(mat1=torch.randn_like(m1), mat2=torch.randn_like(m2)) 

# Inputs to the model are different from each other. For example, the input tensor to the model is torch.randn(3, 5, 64) instead of torch.randn(3, 8, 64).
x1 = torch.randn(3, 5, 64) 
