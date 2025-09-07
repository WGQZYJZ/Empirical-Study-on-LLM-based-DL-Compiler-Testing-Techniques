
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensors = torch.split(v1, [1, 1], dim=-1) # Split the input tensor into two tensors along the third dimension
        concatenated_tensor = torch.cat([split_tensors[0] for i in range(len(split_sizes))], dim=0) # Concatenate the split tensors along the first dimension
        return concatenated_tensor


# Initializing the model
m = Model()


