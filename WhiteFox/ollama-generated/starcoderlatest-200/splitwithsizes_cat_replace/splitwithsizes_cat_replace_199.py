
class Model(torch.nn.Module):
    def __init__(self, split_sizes, dim):
        super().__init__()
        self.split_sizes = split_sizes
        self.dim = dim
 
    def forward(self, x1):
        v1 = torch.split(x1, self.split_sizes, dim=self.dim)
        v2 = torch.cat(v1, dim=self.dim)
        return v2


# Initializing the model
m = Model([64, 64, 3], 0)

# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)
