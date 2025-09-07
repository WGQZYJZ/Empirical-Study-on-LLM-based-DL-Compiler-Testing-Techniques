 
class Model(torch.nn.Module):
    def __init__(self, dim = 2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dim = dim

    def forward(self, x):
        v1 = self.conv(x) # Apply pointwise convolution to the input tensor with kernel size 1 and stride 1

        split_tensors = torch.split(v1, int(v1.shape[self.dim]), dim = self.dim)  # Split the output of the convolution along the given dimension (i.e., split by column) into multiple tensors
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=self.dim)  # Concatenate all the split tensors in the given dimension
        
        return concatenated_tens
