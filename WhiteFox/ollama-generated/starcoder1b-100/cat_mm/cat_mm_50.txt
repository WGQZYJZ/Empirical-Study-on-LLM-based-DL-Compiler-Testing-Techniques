
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2).view(-1, self.dim)


# Initializing the model
m = Model(3)


