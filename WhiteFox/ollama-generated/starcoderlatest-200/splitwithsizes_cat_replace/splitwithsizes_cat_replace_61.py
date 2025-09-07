
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [1024, 64], dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along the same dimension
        return concatented_tensor
 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
