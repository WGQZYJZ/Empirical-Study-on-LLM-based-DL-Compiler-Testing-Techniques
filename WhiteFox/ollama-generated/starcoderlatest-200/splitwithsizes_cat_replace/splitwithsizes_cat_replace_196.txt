
class Model(torch.nn.Module):
    def __init__(self, dim = 0):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        split_tensors = torch.split(v1, split_sizes=[4], dim = dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=dim)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
