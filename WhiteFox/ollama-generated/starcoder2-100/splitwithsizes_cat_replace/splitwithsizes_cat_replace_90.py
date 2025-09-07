
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 256, dim=3) # Split the input tensor into tensors along dimension 3 with size 256 for each of the split tensors
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=3) # Concatenate the split tensors along dimension 3 to form a larger tensor of size [1, 3, 256 * len(split_tensors), 256].
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4097, 8)

__output__  = m(x1)

