
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2)
        return torch.cat([v1], dim=3), None


# Initializing the model
m  = Model()
__output__, __none__  = m(x1)

