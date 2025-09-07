
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [1, 4, 2]
        return is_valid_splitwithsizes_cat(self, x1, split_sizes)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
