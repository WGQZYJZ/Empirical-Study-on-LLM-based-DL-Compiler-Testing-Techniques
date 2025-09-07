
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, split_sizes=[1], dim=1)  # Split the input tensor into several tensors along a given dimension
        v3 = torch.cat([v2[i] for i in range(len(split_sizes))], dim=1)  # Concatenate the split tensors along the same dimension
        return v3

