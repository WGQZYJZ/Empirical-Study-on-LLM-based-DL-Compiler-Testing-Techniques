
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.split(x1, 3, dim=1) # Split along dimension 1 into three tensors along with dimension 0 (along width)
        v2 = torch.cat([v[i] for i in range(len(v))], dim=0) # Concatenate the split tensors along the same dimension
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 5, 64, 64)
