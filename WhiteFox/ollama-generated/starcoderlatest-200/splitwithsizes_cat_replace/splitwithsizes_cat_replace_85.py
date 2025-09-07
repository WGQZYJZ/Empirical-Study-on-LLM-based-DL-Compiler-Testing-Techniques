
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [4, 2, 2], dim=1) # Split the input tensor into 3 tensors along dimension 1 (height). In this way we can generate a model with one torch.cat operation instead of two. 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along the same dimension
        v2 = self.conv2(concatenated_tensor)
        return v6

