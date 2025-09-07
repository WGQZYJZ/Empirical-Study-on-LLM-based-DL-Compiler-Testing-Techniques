
class Model(torch.nn.Module):
    def __init__(self, n_split):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.n_split = n_split
 
    def forward(self, x1):
        split_tensors = torch.split(x1, self.n_split, dim=-1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-1) 
        return concatttened_tensor

# Initializing the model
m = Model(5)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
