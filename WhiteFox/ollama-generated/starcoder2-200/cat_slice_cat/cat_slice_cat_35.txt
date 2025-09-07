
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1s):
        v0 = torch.cat([x for x in x1s], dim=1)
        v3 = torch.slice(v0, 0, 9223372036854775807)
        v4 = torch.slice(v3, 0, size)
        return torch.cat([v0, v4], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1s = [torch.randn(size, 9223372036854775807), torch.randn(size - size // 2)] # Generate two input tensors that are concatenated along dimension 1 and then further sliced along the same dimension
