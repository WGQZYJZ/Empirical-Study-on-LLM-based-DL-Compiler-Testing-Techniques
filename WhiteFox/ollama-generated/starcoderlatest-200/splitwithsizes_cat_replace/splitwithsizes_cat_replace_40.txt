
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.split_sizes = [32] * 6
        self.dim = dim
 
    def forward(self, x1):
        t1 = torch.split(x1, self.split_sizes[0], self.dim) # Split the input tensor into several tensors along a given dimension
        t2 = torch.cat([t1[i] for i in range(len(self.split_sizes))], self.dim) # Concatenate the split tensors along the same dimension
        return t2
