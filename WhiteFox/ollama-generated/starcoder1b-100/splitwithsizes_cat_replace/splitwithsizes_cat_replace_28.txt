
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[i] for i in range(len(x1.shape))] # The size of each tensor along the corresponding dimension
        split_tensors = torch.split(x1, split_sizes, dim=-2)  # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-2)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()
x1 = torch.randn(3, 8, 64, 64)
