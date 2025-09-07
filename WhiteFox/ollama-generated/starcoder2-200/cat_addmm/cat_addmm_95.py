
class Model(torch.nn.Module):
    def __init__(self, num_classes=10, dim=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 7)
 
    def forward(self, x1):
         t1  = torch.addmm(x1, mat1, mat2) 
         t2  = torch.cat([t1], dim=dim)
         return t2

# Initializing the model
m = Model()

 # Inputs to the model
input_tensor   = torch.randn(10, 3, 64, 64)
mat1           = torch.zeros((8, 9), requires_grad=True).requires_grad_(True)
mat2           = torch.ones ((9,),    requires_grad=True).requires_grad_(True)

# Running the model to generate a dynamic trace
__output__  = m(input_tensor, mat1, mat2)

