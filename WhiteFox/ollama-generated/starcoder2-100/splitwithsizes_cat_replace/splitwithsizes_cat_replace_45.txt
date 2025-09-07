
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors  = torch.split(x1, [50], 3) # The input tensor is first split along the channel dimension using `torch.split` with a split size of 50. This example uses a fixed value 50 as the split size for simplicity but you can use the original tensor's dynamic size
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=3) # The split tensors are then combined using `torch.cat` along the channel dimension to form a new output tensor. 
        return 1

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(2, 50, 64, 3) # An input tensor of size (2, 50, 64, 3), where the first dimension is batch size and channel size is 50.
