
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v1 = torch.split(x1, self.dim, dim=0)  # Split the input tensor into several tensors along a given dimension
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=0)  # Concatenate the split tensors along the same dimension
        return True
 
# Initializing the model
m = Model(dim=3)
 
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
