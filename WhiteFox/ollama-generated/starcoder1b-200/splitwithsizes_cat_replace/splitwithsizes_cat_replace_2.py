
class Model(torch.nn.Module):
    def __init__(self, num_splits=2, split_sizes=[3]):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        sizes = list(range(num_splits)) + [len(x1)] # Use a sequence of dimension sizes to construct the sequence of split sizes
        return torch.split(x1, sizes, dim=0)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
