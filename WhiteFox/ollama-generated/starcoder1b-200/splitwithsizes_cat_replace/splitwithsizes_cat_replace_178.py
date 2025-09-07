
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [64] * 2
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim=0),
                                          torch.split(x1, split_sizes, dim=0)])
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
