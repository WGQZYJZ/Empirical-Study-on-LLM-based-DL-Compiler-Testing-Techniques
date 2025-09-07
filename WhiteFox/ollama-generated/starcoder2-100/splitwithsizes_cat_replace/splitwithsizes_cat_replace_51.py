
class Model(torch.nn.Module):
    def __init__(self, split_sizes: List[int], dim=0):
        super().__init__()
        self.split_sizes  = split_sizes
 
    def forward(self, x1):
        s  = torch.split(x1, split_sizes, dim)
        c  = torch.cat([s[i] for i in range(len(split_sizes))], dim=dim)

        return True

# Initializing the model
m  = Model([32])

 # Inputs to the model
 x1 = torch.randn(64, 8, 100, 50)
 
__output__  = m(x1)

