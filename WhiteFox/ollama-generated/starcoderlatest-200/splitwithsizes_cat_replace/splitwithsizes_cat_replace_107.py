
class Model(torch.nn.Module):
    def __init__(self, input_size=64, num_splits=3):
        super().__init__()
        self.input_size = input_size
        self.num_splits = num_splits
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [self.input_size for i in range(self.num_splits)], dim=3) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=3) # Concatenate the split tensors along the same dimension
        return concatenated_tensor

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
