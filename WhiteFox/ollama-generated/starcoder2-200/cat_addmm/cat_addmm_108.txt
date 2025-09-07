
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm  = torch.nn.functional.linear
 
    def forward(self, x1, m1, m2):
        v1  = self.addmm(x1, m1, m2) # Perform a matrix multiplication of mat1 and mat2
        return torch.cat([v1], dim=0)


# Initializing the model
m  = Model()
 
 # Inputs to the model 
 x1  = torch.randn(3, 64)
 m1  = torch.ones((3, 3), requires_grad=True)
 m2  = torch.zeros((3, 9), requires_grad=True)

 # Outputs from the model 
 __output__   = m(x1, m1, m2)
