
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return is_valid_splitwithsizes_cat([
            torch.split(x1, split_sizes, dim)[0] for dim, split_sizes in self.get_valid_dim_order().items()
        ])
 
    def get_valid_dim_order(self):
        return {i: [j] for i in range(self.conv.out_channels) for j in [i, i + 1]}

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
