
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        split_sizes = [4] + [4 for _ in range(9)]
        v1 = torch.cat([torch.split(x, split_sizes, dim)[i] for i in range(len(split_sizes))], dim=0)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(32, 3, 64, 64)
