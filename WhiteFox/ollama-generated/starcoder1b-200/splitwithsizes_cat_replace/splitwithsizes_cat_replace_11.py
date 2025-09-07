
class Model(torch.nn.Module):
    def __init__(self, n_splits=5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [64] * (n_splits + 1)  # Split dimension is the length of this list.
        concat_tensor = torch.cat([torch.split(x1, split_sizes[i], dim=dim) for i in range(len(split_sizes))], dim)
        return torch.cat((self.conv(concat_tensor), 0), dim=0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
