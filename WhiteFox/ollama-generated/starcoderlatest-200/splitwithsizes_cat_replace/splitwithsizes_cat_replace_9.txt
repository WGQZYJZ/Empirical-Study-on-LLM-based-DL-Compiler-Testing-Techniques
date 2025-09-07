
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 3, dim=1) # Split the input tensor into three tensors along dimension 1 (i.e., channel axis)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate all of the split tensors along dimension 1 (i.e., channel axis)
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
