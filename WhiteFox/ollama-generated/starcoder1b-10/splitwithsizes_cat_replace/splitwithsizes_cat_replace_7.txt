
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [64, 32]
        concatenated_tensor = torch.split(x1, split_sizes, dim=1)  # Split the input tensor into several tensors along a given dimension
        return torch.cat([torch.mul(x1[i], 0.5) for i in range(len(split_sizes))])


# Initializing the model
m = Model()


