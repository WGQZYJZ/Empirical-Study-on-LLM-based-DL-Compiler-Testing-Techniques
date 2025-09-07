
class Model(torch.nn.Module):
    def __init__(self, dimension):
        super().__init__()
        self.dimension = dimension
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1], dim=self.dimension)
        return v2


# Initializing the model
m = Model(3)

# Inputs to the model
x1 = torch.randn(2, 4, 8, 5)
x2 = torch.randn(2, 4, 6, 9)
