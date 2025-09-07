
class Model(torch.nn.Module):
    def __init__(self, split_dim=1):
        super().__init__()
 
    def forward(self, x):
        # Splitting
        a  = torch.split(x, [32], dim)
        b  = torch.cat([a[0], a[-1]], dim)
        
        # Concatenating 
        c  = torch.cat([b[i] for i in range(len(split_sizes))], split_dim=split_dim)
    
        return c

# Initializing the model with the default split dimension value of 3. 
m  = Model()
 
# Inputs to the model with the default split dimension value of 1
x2  = torch.randn(64, 80, 75).split(40)
__output__  = m(x2)

