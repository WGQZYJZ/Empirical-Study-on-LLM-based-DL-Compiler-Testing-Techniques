
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        return 1 + arg2
 
 # Initializing the model
m = Model()

# Inputs to the model
arg1  = torch.full([1], 1, dtype=dtype, layout=layout, device=device)
arg2  = torch.full([3], 2, dtype=dtype, layout=layout, device=device)
