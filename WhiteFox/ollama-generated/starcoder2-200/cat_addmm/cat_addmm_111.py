
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # The input to the model must be a single tensor of shape (1, 3072)
        mat = torch.rand((3072, 5)) 
        mat1 = torch.randn((3072, 4))
        mat2 = torch.randn((3072, 8))
        v1  = x1.addmm(mat, mat1, mat2)
        return v1


# Initializing the model