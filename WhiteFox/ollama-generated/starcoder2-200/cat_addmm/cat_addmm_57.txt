
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
        self.dim  = dim

    def forward(self, x1):

        v1  = torch.addmm(x1, mat1, mat2) 
        v2  = torch.cat([v1],self.dim)
        
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
mat1  = torch.randn(50,30).cuda().float()
mat2  = torch.randn(30,8).cuda().float()
x1  = torch.randn(16,3,4,4)
__output__  = m(x1)

