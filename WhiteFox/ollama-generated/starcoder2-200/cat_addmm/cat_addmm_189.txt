
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1  = torch.addmm(x1, mat1, mat2) 
        return t1

 # Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(37, 48960) + 5 
mat1= torch.ones((48960, 4)) * 3.253864e-01
mat2= torch.ones((4, 50)) * 7.877470e+01
 
