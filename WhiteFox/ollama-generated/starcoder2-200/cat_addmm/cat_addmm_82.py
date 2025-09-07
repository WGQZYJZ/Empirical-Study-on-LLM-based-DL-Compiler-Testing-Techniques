
class Model(torch.nn.Module):
    def __init__(self, dim1=0):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.addmm(x1[dim], self._mat1_, self._mat2_)
        v3  = torch.cat([v2], dim) 
        return v3
 
m  = Model(0)

 # Inputs to the model
 _mat1_ = torch.randn(64, 512).view(-1, 8, 8)
 _mat2_= torch.randn(512, 793).view(8, -1)
 x1 = [torch.randn(10, 8)]
 
# Initializing the model and setting model attributes for this model:
m._mat1_  =  _mat1_
m._mat2_  =   _mat2_

 # Executing the model with inputs:
 