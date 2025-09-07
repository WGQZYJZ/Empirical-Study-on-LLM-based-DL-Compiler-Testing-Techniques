
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[], dim=-1):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, split_sizes, dim)  # split
        return torch.cat([v[i] for i in range(len(split_sizes))], dim)
 
 # Initializing the model
m  = Model([], -1)
 
# Inputs to the model