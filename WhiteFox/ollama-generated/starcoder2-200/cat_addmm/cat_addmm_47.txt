
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim):
        super().__init__()
 
        self.add  = torch.nn.Identity()
        self.cat = torch.nn.Identity()
        self._dim = dim
        self.linear  = torch.nn.Linear(mat1.shape[0], mat1.shape[1])
 
    def forward(self, x):
        self.linear.weight = mat1
        v1  = self.add(x) # Add the input to the result of matrix multiplication 
        v2 = v1 + mat2 # Add another tensor to the result of matrix multiplication
        
        v3 = self.cat([v2], dim=self._dim)
 
        return v3
 
m = Model(mat1, mat2, 0)


# Initializing the model
__model_output__ = m(__input__)


