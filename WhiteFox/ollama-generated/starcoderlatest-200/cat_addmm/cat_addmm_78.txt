
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, mat1, mat2)
        t2 = torch.cat([t1], dim=0)
        return t2

# Inputs to the model
mat1 = torch.randn(24, 6, 5, 8) # Random matrix with shape [24, 6, 5, 8]
mat2 = torch.randn(24, 3, 4, 7) # Random matrix with shape [24, 3, 4, 7]
