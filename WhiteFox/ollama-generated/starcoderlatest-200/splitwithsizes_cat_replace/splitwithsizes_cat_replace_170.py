
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        split_tensors = torch.split(v1, [2, 3], dim)  # Split the output of the convolution into two tensors along dimension dim=1
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) # Concatenate the split tensors along the same dimension
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
