
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes, dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        v  = self.split_conv(concatenated_tensor)
        return v


# Split sizes
split_sizes = [32, 8, 4, 4, 1]
