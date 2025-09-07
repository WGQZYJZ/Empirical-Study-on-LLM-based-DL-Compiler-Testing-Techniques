
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        split_tensors = torch.split(v1, [2, 4], dim=1) # Split the output of convolution along dimension 1
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along the same dimension
