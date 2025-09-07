
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, split_sizes):
        v1 = self.conv(x1)
        v2 = split_tensors[0] * 0.5
        v3 = split_tensors[1] * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Input tensors to the model
input_tensor = torch.randn(1, 3, 64, 64)
split_sizes = [64, 1]
