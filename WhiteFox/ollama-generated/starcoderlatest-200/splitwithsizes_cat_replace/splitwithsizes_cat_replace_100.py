
class Model(torch.nn.Module):
    def __init__(self, n=2, d=3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(n, d, 1)
        self.relu = torch.nn.ReLU()
        self.pool = torch.nn.MaxPool2d(kernel_size=4, stride=2, padding=0)
 
    def forward(self, x1):
        t1 = self.conv1(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        split_tensors = torch.split(t1, [1], dim=1) # Split the output of the first convolution into several tensors along dimension 1
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along dimension 1
        v5 = self.pool(concatenated_tensor) # Apply max pooling with a kernel size of 4 and stride 2 to the concatenated tensor
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
