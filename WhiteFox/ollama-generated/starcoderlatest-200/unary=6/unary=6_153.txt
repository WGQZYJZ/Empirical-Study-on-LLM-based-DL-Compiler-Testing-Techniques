
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6


# Generating the input tensor for the model
def test():
    # Generate an input tensor with random values that satisfy all the above requirements and return it.
    x = [torch.randn(1, 3, 64, 64) for _ in range(20)]
    torch.testing.assert_input(m, x)


# Testing
test()
