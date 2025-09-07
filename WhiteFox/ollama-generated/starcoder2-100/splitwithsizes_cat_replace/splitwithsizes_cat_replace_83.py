

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):

        split_tensors  = torch.split(x1, [64], dim=1) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=1)# Concatenate the split tensors along the same dimension
        return concatenated_tensor

# Initializing the model and generating input tensor