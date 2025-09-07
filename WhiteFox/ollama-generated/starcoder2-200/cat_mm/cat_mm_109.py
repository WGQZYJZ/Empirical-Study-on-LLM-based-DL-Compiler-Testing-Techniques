
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2) 
        v01  = v * 3.14 # multiplying the result of matrix multiplication by a constant
        v02  = torch.cat([v01] * 5 + [v01], -1)  
        return v02


# Initializing and testing the model on randomly generated inputs
x1, x2  = torch.randn(3, 64), torch.randn(64, 78) # Generating input tensors of sizes (3, 64), (64, 78). 

m  = Model()
m(x1, x2)

