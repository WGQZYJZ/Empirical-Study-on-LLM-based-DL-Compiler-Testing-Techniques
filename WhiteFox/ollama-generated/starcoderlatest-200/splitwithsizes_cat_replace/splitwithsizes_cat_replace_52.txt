
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes, self.dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=self.dim)
        return concatenated_tensor

# Initializing the model
m = Model(3)
# Split sizes and dimensions can be set to different values to test scenarios with more split sizes and more dimensions. For example, to set dim=0 as the split dimension for a 5-D input tensor of size (1, 2, 4, 8, 16), you can use `split_sizes = [1]` for splitting along the first dimension, or `dim=0` for splitting along dimension 0 and `dim=-1` for splitting along dimension -1.
split_sizes = [2, 4]
