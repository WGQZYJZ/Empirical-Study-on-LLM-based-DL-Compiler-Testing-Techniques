
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [4, 2, 1, 1], dim=-1) # Split input tensor into four subtensors along the third dimension
        
        concatenated_tensor = torch.cat([ # Concatenate these subtensors along the third dimension
            split_tensors[i] for i in range(len(split_sizes))], dim=0)
        return concatenated_tensor


# Initializing the model
m = Model()


