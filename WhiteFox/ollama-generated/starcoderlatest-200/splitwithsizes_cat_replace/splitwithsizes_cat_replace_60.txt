
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 2, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        split_tensors1 = torch.split(v1, [3], dim=1) # Split the output of the convolution along dimension 1 (along axis 1 for 4-d tensors)
        v2 = torch.cat([split_tensors1[i] for i in range(len(split_sizes))], dim=1)
        v3 = self.conv2(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
