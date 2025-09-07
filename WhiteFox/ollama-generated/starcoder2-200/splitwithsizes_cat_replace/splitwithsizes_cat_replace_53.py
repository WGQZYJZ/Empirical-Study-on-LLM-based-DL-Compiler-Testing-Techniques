
class Model(torch.nn.Module):
    def __init__(self, split_sizes=None, dim=-1):
        super().__init__()
 
    def forward(self, x2):
        v7  = torch.split(x2, split_sizes)
        v8  = torch.cat([v7[i] for i in range(len(split_sizes))], dim)


# Initializing the model
m = Model()

# Inputs to the model
x104654  = torch.randn(3, 2)
 
__output__  = m(x104654)
 
