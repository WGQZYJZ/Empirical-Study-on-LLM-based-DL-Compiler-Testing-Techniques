
class Model(torch.nn.Module):
    def __init__(self, dim_tensor: int = 1):
        super().__init__()
        self.dim = dim_tensor
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * 3, self.dim)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
