
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        v1 = torch.cat([x0, x1], dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:size] # Further slice the tensor along dimension 1
        return torch.cat([v1, v3], dim=1)


# Initializing the model and setting inputs/outputs
m = Model()
out = m(x0, x1)
x0  = torch.randn(4, 9223372036854775807)
x1  = torch.randn(size, size*size+32)

