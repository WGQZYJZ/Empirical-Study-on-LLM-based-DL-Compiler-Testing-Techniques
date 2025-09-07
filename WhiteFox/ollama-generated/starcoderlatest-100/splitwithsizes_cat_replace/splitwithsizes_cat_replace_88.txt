
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes, dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return True


# Initializing the model
m = Model()

# Inputs to the model
split_sizes = [16, 24, 80, 32] # The size of each split tensor
x1 = torch.randn(1, 3, 64, 64)
