
class Model(torch.nn.Module):
    def __init__(self, size=327680):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat(x1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m  = Model(size=1<<31-96+1) # size is the number of elements to be sliced
 
# Inputs to the model
__inputs__  = [torch.randn(1, n, 2054)] * 8
 
