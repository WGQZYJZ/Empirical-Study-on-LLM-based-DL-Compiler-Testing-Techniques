
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[128, 64], dim=0):
        super().__init__()
        self.split_sizes = split_sizes
        self.dim = dim
 
    def forward(self, x1):
        split_tensors = torch.split(x1, self.split_sizes, dim=self.dim) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(self.split_sizes))], dim=self.dim) 
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
