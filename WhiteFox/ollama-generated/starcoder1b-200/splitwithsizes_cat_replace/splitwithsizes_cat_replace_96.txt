
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[dim] for dim in range(len(x1.shape))]
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim) for dim in range(len(x1.shape))])
        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
