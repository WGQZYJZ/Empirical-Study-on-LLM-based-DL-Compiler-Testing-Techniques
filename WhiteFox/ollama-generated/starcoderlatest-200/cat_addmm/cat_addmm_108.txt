
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat1 = torch.randn(8, 4, bias=False)
        self.mat2 = torch.randn(8, 6, bias=False)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=dim)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 