
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.addmm(x1, mat1, mat2)
        v3  = torch.cat([v2], dim) # This is the concatenation line
        return v3

# Initializing the model
m = Model()
