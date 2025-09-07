
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = (3, 64)
        concatenated_tensor = torch.cat([torch.split(v1, sizes, dim) for sizes in split_sizes], dim=0)
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 1, 64, 64)
