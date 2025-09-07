
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v1 = torch.split(x1, [8, 4, 2], self.dim) # Split the input tensor into three tensors along the third dimension
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=self.dim) # Concatenate the split tensors along the third dimension
        return v2

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
split_sizes = [8, 4, 2]
dim = 3
