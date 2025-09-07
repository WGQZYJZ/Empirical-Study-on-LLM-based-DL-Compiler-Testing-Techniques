
class Model(torch.nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def forward(self, x1):
        t1 = torch.split(x1, 3, dim=2)
        t2 = [t1[i] for i in range(len(t1))] # Apply a function f_i to each tensor t1_i
        return torch.cat(t2, dim=0)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
