
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 4096, dim=3) # Split the input tensor into several tensors along a given dimension 
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=3) # Concatenate the split tensors along the same dimension
        return v2


# Input shape
__input_1__ = 64, 64, 3

