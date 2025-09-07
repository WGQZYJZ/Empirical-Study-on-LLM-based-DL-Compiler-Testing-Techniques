
class Model(torch.nn.Module):
    def __init__(self, split_sizes, dim=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes, dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) 
        return concatenated_tensor


# Initializing the model
m = Model(torch.Size([2])) # Please replace "torch.Size([2])" with public PyTorch APIs you want to split, such as "torch.size()".


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
