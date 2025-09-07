
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, tens):
        v1 = torch.cat(tens, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[::size, :] # Slicing the tensor along dimension 1 with a size 64 (sice 1, size 64, size -1)
        v4 = torch.cat([v1, v3], dim=1)
 
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = [torch.randn(size_i, 50)] # Tensor input with size i = random_int(32, 96)
__output__  = m(x1)

