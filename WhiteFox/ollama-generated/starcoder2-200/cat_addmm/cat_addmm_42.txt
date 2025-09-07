
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2) 
        return v1

