
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x, y):
        v  = torch.matmul(x, y)
        v2 = v + self.dim
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
y1 = torch.randn(2, 8)
