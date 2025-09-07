
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.split_sizes  = [1] + [(2**i) for i in range(-50, -49)]
        self.concat_indices = list(range(len(self.split_sizes)))
 
    def forward(self, x1):
        self.split_tensors = torch.split(x1, split_sizes=self.split_sizes, dim=-2) # Split the input tensor into several tensors along a given dimension of size 32
        concatenated_tensor = torch.cat([self.split_tensors[i] for i in self.concat_indices], -2) # Concatenate the split tensors along the same dimension of size 16, 4, ..., 0.5^(-50:=-49), 1
        return concatenated_tensor


# Initializing the model