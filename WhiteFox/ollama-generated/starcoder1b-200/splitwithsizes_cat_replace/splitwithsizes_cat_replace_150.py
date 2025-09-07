
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes  = (1, 4)
        concatenated_tensor  = torch.cat([torch.split(x1, split_sizes, dim=1),
                                         torch.split(x1, split_sizes, dim=0)],
                                        dim=1)
        is_valid_splitwithsizes_cat  = (concatenated_tensor != x1).any()
        v2  = self.conv(concatenated_tensor) * 0.5
        return v2 if is_valid_splitwithsizes_cat else torch.nn.functional.erf(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
