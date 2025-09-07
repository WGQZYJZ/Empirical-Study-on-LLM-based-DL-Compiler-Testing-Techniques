
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1,x2):
        v3 = torch.mm(x1, x2) # matrix multiplication between input1 and input 2
        v4 = torch.mm(x1 + x2, 0.5)  # Addition of the results of two matrix multiplications then multiplying by a constant .5 
        v6 = v3 * 0.7071067811865476
        v7 = torch.erf(v6)  # Apply error function on the output of the multiplication
        v8 = v4 + v7  # Addition between the two matrix multiplications and the error function outputs 
        return v3 * v4
 
# Initializing the model    
m1 = Model()
    
# Inputs to the model
x1 = torch.randn(2, 5) # random inputs with 2 rows of length 5 
x2 = torch.randn(3, 7) # random inputs with 3 rows and length 7
 
__output__  = m1(x1, x2)

