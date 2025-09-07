

class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor, mat2: torch.Tensor):
        super().__init__()
        self.mat1 = mat1 
        self.mat2  = mat2
        
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        t1  = torch.addmm(input, self.mat1, self.mat2)
        t2  = torch.cat([t1], dim=0)
        return t2
        
# Initializing the model
m = Model(torch.randn(32), torch.randn(64))


# Inputs to the model
x1  = torch.randn(8, 32)


