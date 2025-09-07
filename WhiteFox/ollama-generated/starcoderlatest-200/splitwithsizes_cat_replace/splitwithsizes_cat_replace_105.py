
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0)
 
    def forward(self, x):
        split_tensors = torch.split(x, 3, dim=1) # Split the input tensor into several tensors along dimension with index 1 (which corresponds to `torch.cat` in this model) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) # Concatenate the split tensors along the same dimension
        v = self.conv2(concatenated_tensor)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
