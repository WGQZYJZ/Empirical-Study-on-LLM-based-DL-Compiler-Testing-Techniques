
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v0  = [x1] + [1 for i in range(4)] # add 4 1s to the input as initial vector
        v1  = torch.addmm(*v0)   # matrix multiplication (x1, v0)
        v2  = torch.cat([v1], dim=0)  # concatenate along dimension 0 
        return v2

# Initializing the model