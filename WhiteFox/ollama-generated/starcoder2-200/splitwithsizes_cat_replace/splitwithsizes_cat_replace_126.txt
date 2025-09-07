
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.split(x1, [32], dim=2) # Split the input tensor into two tensors of size (N/4 x 64 x 57). The first dimension is unchanged since it's 8.
        v1  = torch.split(v0[0], [32] * 3 + [8, 16, 128, 92], dim=1) # Split the first tensor of size (N/4 x 57 x 32) into five tensors: the first one has size 32*n, the rest have sizes 32*(1+n), where n is an integer.
        return torch.cat([v0[i] for i in range(len(v1))] + [v1[-1]], dim=0)


# Initializing the model
m = Model()
# Inputs to the model
x  = torch.randn(32, 8, 57 * 4) # Input tensor has size (N x 64 x 57) but is actually split along its third dimension into four tensors of size (32*n x 64 x 1), where n is an integer


