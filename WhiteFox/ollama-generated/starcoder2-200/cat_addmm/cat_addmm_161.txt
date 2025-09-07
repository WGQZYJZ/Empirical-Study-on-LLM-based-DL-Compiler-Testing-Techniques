
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None, dim=-3):
        super().__init__()
        self.mat1 = torch.randn((64, 5)) if mat1 is None else mat1
        self.mat2 = torch.randn((70, 5)) if mat2 is None else mat2 
        self.dim  = -3 if dim < 0 else dim
    
    def forward(self):
        t1 = torch.addmm(torch.zeros_like(input), self.mat1, self.mat2) # Create a zero tensor of the same size as input and then perform matrix multiplication between self.mat1 and self.mat2. Then add this result to the input.
        return torch.cat([t1], dim=self.dim)

# Initializing the model
m = Model(torch.randn((64, 5)), torch.randn((70, 5)))

