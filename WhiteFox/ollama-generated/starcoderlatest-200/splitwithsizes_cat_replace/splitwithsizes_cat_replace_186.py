
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[10, 2, 3], dim=1):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes, dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return concatenated_tensor


# Input shape: [1, 3, 64, 64]
input_tensor = torch.randn(1, 3, 64, 64)
