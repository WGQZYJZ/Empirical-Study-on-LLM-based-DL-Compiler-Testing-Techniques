
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size=32):
        v1 = torch.cat([x1] * 4)
        v2 = v1[:, 0:size]
        v3 = v2[:, 0:size] # The tensor to slice
        v5 = torch.cat([v1, v3], dim=1)
        return v5

# Initializing the model
m = Model()
x1  = torch.randn(4, 6, size, size).requires_grad_(True)
 
# Calculating the outputs of the model
__output__  = m(x1, size=32)

