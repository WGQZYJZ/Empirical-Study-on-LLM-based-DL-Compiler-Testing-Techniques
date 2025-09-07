
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # The number of channels and output channel numbers are different

    def forward(self, x1):
        v1 = self.conv1(x1) # The first convolution is only used in the concatenation
        split_tensors = torch.split(v1, 2, dim=0) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) # Concatenate the split tensors along the same dimension
        return v6


# Outputs of Torch SSAO: 