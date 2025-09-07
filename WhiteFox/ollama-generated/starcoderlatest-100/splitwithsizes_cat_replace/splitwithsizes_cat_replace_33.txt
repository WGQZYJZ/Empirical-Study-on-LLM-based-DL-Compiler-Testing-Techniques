 with replacements
class MyModel(torch.nn.Module):
    def __init__(self, n_splits=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
        split_sizes = [] # A list to keep track of the indices of `torch.split` in each `forward` call
        for i in range(n_splits):
            t1 = self.conv(x1) # Apply a convolution operation to input tensor 'x1'
            split_sizes += [i] # Save its index
        concatenated_tensor  = torch.cat([t1 for i in range(len(split_sizes))], dim=0) # Concatenate all of the output from the convolution operations
        return (split_sizes, concatenated_index), concat_tensors


# Initializing model with replacements
m2 = MyModel()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
res = m2(x1)
split_sizes, concatenated_index = res[0]
concat_tensors = res[1]


