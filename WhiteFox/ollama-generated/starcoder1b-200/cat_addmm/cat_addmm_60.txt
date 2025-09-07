
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
        self.mat1 = torch.tensor(mat1)
        self.mat2 = torch.tensor(mat2)
 
    def forward(self, x1):
        return torch.cat([torch.addmm(x1, self.mat1, self.mat2)], dim=1)


# Initializing the model
m = Model(mat1=[0, 1], mat2=[3, -2])
