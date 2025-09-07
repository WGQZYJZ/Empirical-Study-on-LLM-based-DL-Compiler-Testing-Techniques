
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensor  = torch.split(input_tensor, split_sizes, dim)  # Split the input tensor into several tensors along a given dimension
        concatenated_tensor  = torch.cat([torch.squeeze(x1 * split_tensor[i], 0) for i in range(len(split_sizes))], dim)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
