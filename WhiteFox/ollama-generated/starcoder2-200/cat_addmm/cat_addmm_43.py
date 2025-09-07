
class Model(torch.nn.Module):
    def __init__(self, mat1):
        super().__init__()
        self.mat1 = mat1
        self.mat2  = torch.randn(3,5)
 
    def forward(self, x): 
        v1  = torch.addmm(x, mat1, mat2)   
        return torch.cat([v1], dim=0)

 # Initializing the model
 m = Model(torch.zeros((7,9)))
 
 