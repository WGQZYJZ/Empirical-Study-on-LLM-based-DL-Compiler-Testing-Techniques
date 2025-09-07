
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
 
        self._mat1 = torch.zeros([3, 4]) if not mat1 else mat1
        self._mat2 = torch.zeros([3, 5]) if not mat2 else mat2
 
    def forward(self, x):
        t1  = torch.addmm(x, self._mat1, self._mat2)
        return torch.cat((t1), dim=0)


# Initializing the model
m  = Model()
m.__dict__["_mat1"]  =  torch.randn(3, 4)
m.__dict__["_mat2"]  =  torch.randn(3, 5)
# Inputs to the model