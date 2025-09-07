
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        # Concatenate tensors along dimension 0
        v = torch.cat([x1, x2, x3], dim=0)
        # Reshape the concatenated tensor into a new one with dimension 1x6
        t = v.view(v.size(0), -1)
        # Apply linear transformation on the reshaped tensor and return output
        return torch.linear(...)


# Input
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 2, 2)
x3 = torch.randn(1, 4, 2)
