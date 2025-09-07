
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self):
        v1 = torch.full([arg1, arg2], 1)
        v2 = torch.from_numpy(v1.numpy())
        v3 = torch.cumsum(v2, dim=0) # Add cumulative sum to the first row of v2 
        return v3

# Initializing model
m = Model()

