
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self._mat1, self._mat2)  # Add an element-wise matrix multiplication between mat1 and mat2 with x1
        v2 = torch.cat([v1], dim=dim)  # Concatenate the result along a specified dimension to v1
        return v2


# Initializing the model
m = Model(0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
