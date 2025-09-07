
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensors = torch.split(v1, [1], dim=0) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0) # Concatenate the split tensors along the same dimension
#         return torch.max(v1, v2)
        return concatenated_tensor
 
 # The model above can be replaced with the following model. This model does not use any split or concatenation operations, but it uses two consecutive pointwise convolutions and 2 consecutive pointwise batch normalization layers.
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
__input__  = torch.randn(8, 3, 64, 64)
