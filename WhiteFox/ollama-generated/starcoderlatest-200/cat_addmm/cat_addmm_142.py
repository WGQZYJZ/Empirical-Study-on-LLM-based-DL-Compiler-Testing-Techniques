
class Model(torch.nn.Module):
    def __init__(self, mat1_tensor: torch.Tensor):
        super().__init__()
        self.mat1 = mat1_tensor
 
    def forward(self, x1, x2):
        t1  = torch.addmm(x1, self.mat1, x2)
        t2  = torch.cat([t1], dim=3) # Concatenate the result along the third dimension
        return t2

# Inputs to the model
x1 = torch.randn(1, 8096, 4)
