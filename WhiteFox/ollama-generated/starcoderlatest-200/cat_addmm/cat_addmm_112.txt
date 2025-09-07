
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, kernel_size=1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.conv.weight, None) # t1: addmm operation, (n1, n2), [t1] -> ([t1]), [mat1, mat2]-> [[[t1]]], None-> []
        v2 = torch.cat([v1], dim=0)  # Concatenate the result along a specified dimension: t2: cat operation, (n1, d1, d2, d3), [[[t1]]] -> ([[[t1]]]), [dim]-> []
        return v2


# Initializing the model
m = Model(dim=0) # dim == 0 means to concat along dimension 0

# Inputs to the model
x1 = torch.randn(1, 16, 40, 50) # (n1, n2, d1, d2), t1: addmm operation, (n1, n2), [t1] -> ([t1]), [mat1, mat2]-> [[[t1]]], None-> []
