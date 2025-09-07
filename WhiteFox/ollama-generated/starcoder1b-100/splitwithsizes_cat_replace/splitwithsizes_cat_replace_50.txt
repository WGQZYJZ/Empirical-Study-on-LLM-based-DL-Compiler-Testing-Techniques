
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [3] * len(x1.shape) # For example:
        concatenated_tensor  = torch.cat([torch.split(x1, split_sizes, dim) for i in range(len(split_sizes))], dim)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


