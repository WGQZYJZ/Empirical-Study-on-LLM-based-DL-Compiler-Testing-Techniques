
class Model(torch.nn.Module):
    def __init__(self, split_sizes=None):
        super().__init__()
 
    def forward(self, x1): 
        v1  = torch.split(x1, split_sizes)
        v2  = torch.cat([v1[i] for i in range(len(split_sizes))], dim=0)
        return v2

 # Initializing the model
split_sizes = [34856, 34870, 980, 980]
m = Model(split_sizes)
 
 # Inputs to the model
x1 = torch.randn(sum(split_sizes), 128, 128)
  __output__  = m(x1)
