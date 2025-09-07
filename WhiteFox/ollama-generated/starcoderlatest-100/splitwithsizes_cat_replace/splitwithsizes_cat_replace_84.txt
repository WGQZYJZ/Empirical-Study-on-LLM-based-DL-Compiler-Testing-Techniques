
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        split_tensors = torch.split(v1, [32], dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) 
        return torch.nn.ReLU()(concatenated_tensor)


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
