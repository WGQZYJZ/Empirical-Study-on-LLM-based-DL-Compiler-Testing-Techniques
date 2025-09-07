
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2) # Add the output of the multiplication to a random input tensor 
        v2 = torch.cat([v1], 0)
        return v2

m = Model()

