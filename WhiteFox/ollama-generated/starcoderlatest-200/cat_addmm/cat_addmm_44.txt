
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat1 = torch.randn(3, 8) * 0.5 + 0.25
        self.mat2 = torch.randn(16, 8) * 0.7071067811865476 - 1

    def forward(self, x):
        t1 = torch.addmm(x, self.mat1, self.mat2) # The first matrix multiplication in the pattern will be performed here
        t2 = torch.cat([t1], dim=dim) # dim: 1 for a batch axis
        return t2


# Initializing the model
m = Model(dim=1) # Add an extra dimension with dim=1

# Inputs to the model
x = torch.randn(4, 3, 64, 64)
