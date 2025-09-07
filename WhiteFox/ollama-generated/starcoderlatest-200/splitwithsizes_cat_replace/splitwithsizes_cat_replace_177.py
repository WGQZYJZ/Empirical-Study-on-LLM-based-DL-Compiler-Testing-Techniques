
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes=[1], dim=-3) # Split the input tensor into several tensors along the channel dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=-3) # Concatenate the split tensors along the same dimension
 
        return True


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
