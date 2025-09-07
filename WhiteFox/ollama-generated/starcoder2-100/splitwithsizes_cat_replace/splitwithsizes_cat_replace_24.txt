
class Model(torch.nn.Module):
    def __init__(self, split_sizes, dim = 1):
        super().__init__()

    def forward(self, x1):
       return torch.split(x1, split_sizes, self.dim)

# Initializing the model with the specified values of `split_sizes` and `dim`:
m = Model(2048)

