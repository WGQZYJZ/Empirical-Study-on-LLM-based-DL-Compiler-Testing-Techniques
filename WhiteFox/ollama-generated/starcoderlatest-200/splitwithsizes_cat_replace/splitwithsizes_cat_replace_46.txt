
class Model(torch.nn.Module):
    def __init__(self, split_sizes):
        super().__init__()
        self.split_sizes = split_sizes
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.split(v1, self.split_sizes, dim=-1)[0] * 0.5
        return v2


# Inputs to the model
split_sizes = [4, -2]
input_tensor = torch.randn(2, 3, 64, 64)
