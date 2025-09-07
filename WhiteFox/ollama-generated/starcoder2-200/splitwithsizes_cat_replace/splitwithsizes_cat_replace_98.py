

class Model(torch.nn.Module):
    def __init__(self, split_sizes=[3], dim=0):
        super().__init__()
 
    def forward(self, x1):
        splits  = torch.split(x1, split_sizes, dim)
        conct_res  = torch.cat([splits[i] for i in range(len(split_sizes))], dim) 
        return conct_res

# Initializing the model with `split_sizes=[3]` and `dim=0`
m = Model()
x1 = torch.rand(8, 24, 64, 64)
__output__  = m(x1)

