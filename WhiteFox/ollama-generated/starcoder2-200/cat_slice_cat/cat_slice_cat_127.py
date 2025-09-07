
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) 
        v2 = v1[:, 0:9223372036854775807] 
        v3 = v2[:, 0:size] 
        v4 = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model with size parameter equal to 9223372036854775807 and input tensors x1 of shape (1, 9223372036854775807) and x2 of shape (1, size).
m = Model(size=9223372036854775807)
x1 = torch.randn(1, 9223372036854775807)
x2 = torch.randn(1, size)
__output__  = m(x1, x2).shape

