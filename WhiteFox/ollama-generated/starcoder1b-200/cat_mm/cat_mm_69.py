
class Model(torch.nn.Module):
    def __init__(self, dimension: int = 3):
        super().__init__()
        self.dimension = dimension
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2)
        return torch.cat([v, v], dim=self.dimension)


# Initializing the model
m = Model()


