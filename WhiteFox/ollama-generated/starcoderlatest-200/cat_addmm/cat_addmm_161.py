
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

