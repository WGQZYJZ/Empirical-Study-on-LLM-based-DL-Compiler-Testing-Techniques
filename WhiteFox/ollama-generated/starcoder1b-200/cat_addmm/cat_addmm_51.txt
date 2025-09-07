
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32, 64)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, mat)
        v2 = torch.cat([v1], dim)
        return v2


# Inputs to the model
input  = torch.randn(10, 3, 8, 8)  # Batch size: 10
mat1   = torch.randn(64, 32)        # First row of first column of mat
mat2   = torch.randn(32, 64)        # Second row of first column of mat
