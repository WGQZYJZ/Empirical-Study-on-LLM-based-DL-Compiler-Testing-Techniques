
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
        self.linear  = torch.nn.Linear(4*100-dim, 5)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2) 
        v2  = torch.cat([v1], dim=3) # Concatenate the result along a specified dimension
        return self.sigmoid(v2)

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(40, 64*64)
 
 