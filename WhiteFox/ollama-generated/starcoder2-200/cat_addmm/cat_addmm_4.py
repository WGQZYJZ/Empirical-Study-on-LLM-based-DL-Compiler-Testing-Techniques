
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.ops.torch.addmm
 
    def forward(self, x1, mat1, mat2, dim):
        v0  = (x1.size(-1),)
        v1  = torch.zeros(*v0).cuda()
        v3  = self.addmm(v1, mat1, mat2)
 
        return torch.cat([v3], -1)
# Initializing the model
m = Model()

 # Inputs to the model