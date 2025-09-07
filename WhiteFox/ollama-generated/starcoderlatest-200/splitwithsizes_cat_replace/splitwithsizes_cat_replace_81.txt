
class Model(torch.nn.Module):
    def __init__(self, in_channels=3):
        super().__init__()
        self.split_sizes = [64] * 7  # All input tensors are of dimensions (in_channels, split_size1, split_size2, ..., split_sizen).
        self.conv = torch.nn.Conv2d(in_channels=3, out_channels=8, kernel_size=(1, 1), stride=1, padding=0)
 
    def forward(self, x):
        split_tensors = [torch.split(x, self.split_sizes[i], dim=i)[0] for i in range(len(self.split_sizes))]
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=i) # Concatenate the split tensors along dimension 3
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(1, 64, 256, 256)
