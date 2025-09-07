
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensors = torch.split(v1, [4, 5], dim) # Split the output of the convolution into several tensors along dimension 0 (depth axis).
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0) # Concatenate the split tensors along the same depth axis.
        return v6
