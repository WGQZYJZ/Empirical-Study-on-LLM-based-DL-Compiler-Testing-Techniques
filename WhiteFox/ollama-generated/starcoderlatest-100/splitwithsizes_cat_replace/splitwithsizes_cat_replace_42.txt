
class Model(torch.nn.Module):
    def __init__(self, x_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = (64, ) * len(x1.shape[1:])
        split_tensors = torch.split(x1, split_sizes, dim=-2) # Split the input tensor into several tensors along the second dimension, which is the third from the end
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-2) # Concatenate the split tensors along the same dimension
        x4 = self.conv(concatenated_tensor)
        return x4


# Expected output
x1 = torch.randn(1, 3, 64, 64)
