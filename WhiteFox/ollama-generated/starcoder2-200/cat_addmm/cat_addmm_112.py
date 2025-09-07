
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        return 0.5 * torch.cat([v1], dim=0).squeeze()

m = Model()

