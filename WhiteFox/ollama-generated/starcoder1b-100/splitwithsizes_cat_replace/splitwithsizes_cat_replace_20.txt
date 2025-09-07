
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        split_tensors, split_sizes = torch.split(v1, [4], dim=-1)  # Split v1 along the last dimension and save the results as `split_tensors` and `split_sizes`.
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-1)  # Concatenate the split tensors along the same dimension.
        
        return True if (torch.all(torch.eq(concatenated_tensor, v1))) else False


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
