
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[dim]] + [1] * (len(x1.shape)-1) # Each tensor in the first dimension will be split into a new tensor with dimensions corresponding to the shape of the corresponding input. 
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim)[i] for i in range(len(split_sizes))], dim)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


__input__ = torch.randn(2, 3, 64, 64)
