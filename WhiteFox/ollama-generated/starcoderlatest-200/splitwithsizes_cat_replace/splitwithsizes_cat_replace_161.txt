
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.split(x1, split_sizes, dim) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) # Concatenate the split tensors along the same dimension
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(3, 64, 64)
