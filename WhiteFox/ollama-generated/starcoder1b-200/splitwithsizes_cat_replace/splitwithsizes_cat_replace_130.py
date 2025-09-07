
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [v1.shape[0], 1]
        concatenated_tensor = torch.cat([torch.split(v1, sizes, dim=0) for sizes in split_sizes])  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
