
class Model(torch.nn.Module):
    def __init__(self, num_split=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.num_split = num_split
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes=(30//2), dim=3) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=3) # Concatenate the split tensors along the same dimension
        return concatenated_tensor
# Initializing the model
m = Model()


