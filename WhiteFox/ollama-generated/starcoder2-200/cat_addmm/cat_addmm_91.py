
class Model(torch.nn.Module):
    def __init__(self, dim = 0):
        super().__init__()
        
        self.mat1 = torch.randn(32, 3, 64)

        self.mat2 = torch.randn(8, 32)

    def forward(self, x1): 
        v1 = torch.addmm(x1, mat1=self.mat1, mat2=self.mat2)
        v2 = torch.cat([v1], dim = 0)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(48,3,64,64)
 __output__  = m(x1)


