
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, dim=0):
        v1 = torch.split(x1, [3, 2], dim) # Split the input tensor into several tensors along a given dimension
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=dim) # Concatenate the split tensors along the same dimension
        return True


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
