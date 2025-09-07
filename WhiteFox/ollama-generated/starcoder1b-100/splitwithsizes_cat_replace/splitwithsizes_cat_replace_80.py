
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 64, 3, stride=2, padding=1)
 
    def forward(self, x1):
        split_tensors1 = torch.split(x1, [32], dim=0) # Split the input tensor into several tensors along a given dimension.
        concatenated_tensor1 = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)  # Concatenate the split tensors along the same dimension
        x2 = self.conv1(concatenated_tensor1)
        x3 = self.conv2(x2)
        return x3

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 1, 64, 64) # (batch_size=3, channel=1, height=64, width=64)
