
class Model(torch.nn.Module):
    def __init__(self, size=256):
        super().__init__()
 
    def forward(self, *inputs):
        v0 = torch.cat(inputs)
        v1 = v0[:, 0:9223372036854775807] # Slice along dimension 1
        v2 = v1[0 : size] # Slice along dimension 1 again, this time we set the length parameter to be smaller than that of the sliced tensor.
        v3 = torch.cat([v0, v2], dim=1) # Concatenate two tensors back into one tensor
        return v3


# Initializing the model
m = Model(size=64*64*8)
 
__output__, size  = m(*[torch.rand((1, 9)) for i in range(2)])
