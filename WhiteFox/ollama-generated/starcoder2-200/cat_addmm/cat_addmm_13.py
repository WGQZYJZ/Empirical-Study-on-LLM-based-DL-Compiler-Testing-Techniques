
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2):  # Inputs
        v0 = torch.cat([x1], dim)
        v1 = torch.addmm(v0, mat1, mat2)  
        return v1


# Initializing the model