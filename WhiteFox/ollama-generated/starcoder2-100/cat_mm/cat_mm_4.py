
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()
        self.dim  = [dim1 for _ in range(5)] + [-1]
 
    def forward(self, x0, x1):
        v3 = torch.cat([x0], self.dim)
        return v3


# Initializing the model
m  = Model(24, 786)
 
# Inputs to the model
x0  = torch.randn(5, 24, 1952)
x1  = torch.randn(5, 24, 3904)
__output__  = m(x0, x1)

