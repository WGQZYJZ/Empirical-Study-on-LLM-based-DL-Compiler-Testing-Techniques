
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensors = torch.split(v1, 2, dim=1) # Split the output of the convolution into 2 tensors along dimension 1 (axis 1 for PyTorch)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along dimension 1 (axis 1 for PyTorch)
        return v6


# Input to the model
x1 = torch.randn(32, 3, 64, 64)
