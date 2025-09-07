
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 32, dim=0) # Split into 32-D tensors along the dimension 0
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=0) # Concatenate all split tensors along the same dimension
        return v2
 

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(64, 3, 28, 28)
