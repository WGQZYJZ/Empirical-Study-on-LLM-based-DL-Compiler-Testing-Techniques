
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(1, 3, 3)
        self.mat2 = torch.randn(4, 5, 3)
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=0) # Concatenate the output of mat1*mat2 with itself along dimension 0
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(4, 5, 3)
