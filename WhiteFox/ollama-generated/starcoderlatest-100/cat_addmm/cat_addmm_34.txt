
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.tensor([0, 0, 0])
 
    def forward(self, x1, dim=2):
        v1 = torch.addmm(x1, self.mat1, x1)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
dim=0
