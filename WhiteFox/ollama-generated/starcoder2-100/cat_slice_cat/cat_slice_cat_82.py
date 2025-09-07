
class Model(torch.nn.Module):
    def __init__(self, size=4096):
        super().__init__()
 
    def forward(self, *input_tensors): 
        v1 = torch.cat(input_tensors, dim=1)  # Concatenate the input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1 (sliced by `size` and starting at index 0) 
        v3 = torch.cat([v1, v2], dim=1)   # Concatenate the original concatenated tensor with sliced tensor along dimension 1
        return v3

# Initializing the model
m  = Model(4096)

# Inputs to the model
i0  = torch.randn(5, size, dtype=torch.float32)
i1  = torch.randn(7 - size + 5, size, dtype=torch.float32)
i2  = torch.randn(size * 9 + 86 - size, dtype=torch.float32)
__output__  = m(i0, i1, i2)

