
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensor = torch.split(x1, split_sizes, dim)  # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensor[i] for i in range(len(split_sizes))], dim)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


