
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.split(x1, split_sizes, dim)
        return torch.cat([v[i] for i in range(len(split_sizes))], dim)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
