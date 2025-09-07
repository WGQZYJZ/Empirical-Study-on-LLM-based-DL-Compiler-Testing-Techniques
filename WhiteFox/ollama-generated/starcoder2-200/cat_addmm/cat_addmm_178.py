
class Model(torch.nn.Module):
    def __init__(self, mat1):
        super().__init__()
        self.mat2 = torch.randn((38079643,))
        self.mat1 = torch.randn((38079643,), dtype=torch.int)
        self.dim  = 2
 
    def forward(self, input):
        v1 = torch.addmm(input, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn((38079643,))
__output__  = m(x1)


