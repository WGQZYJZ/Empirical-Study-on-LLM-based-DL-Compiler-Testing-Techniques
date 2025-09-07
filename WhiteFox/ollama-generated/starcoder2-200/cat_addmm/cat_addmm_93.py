
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2)
        v3 = torch.cat([v1], dim=0)
        return v3

# Initializing the model