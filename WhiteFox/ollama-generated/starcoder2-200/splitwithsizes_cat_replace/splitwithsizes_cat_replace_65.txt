
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[1], dim=0):
        super().__init__()
 
    def forward(self, x1):
         v2 = torch.split(x1, split_sizes, dim)
         v4 =  [v3 for v3 in v2]
         v5 = torch.cat(v4, dim)
         return v5


# Initializing the model
m  = Model([8], 0)
 
# Inputs to the model
x1  = torch.randn(64*32, 96, 7)
__output__  = m(x1)

