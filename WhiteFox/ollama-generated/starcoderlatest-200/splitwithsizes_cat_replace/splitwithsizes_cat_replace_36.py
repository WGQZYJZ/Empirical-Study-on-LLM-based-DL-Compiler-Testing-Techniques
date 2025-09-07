
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        split_tensors1 = torch.split(x, [40], dim=1)
        concat_tensor1 = torch.cat([split_tensors1[i] for i in range(len(split_sizes))], dim)
 
        v2 = self.conv2(concat_tensor1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
