
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.conv_transpose2d(x1, [64, 64], [3, 8], stride=1, padding=1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 3)  # TODO: use pow(Tensor other, double power) -> Tensor
        v4 = F.conv_transpose2d(torch.pow(v3, 3), [64, 64], [8, 8], stride=1, padding=0)
        v5 = torch.exp(v4)
        v6 = F.conv_transpose2d(v5 + 1, [64, 64], [3, 3], stride=1, padding=1)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
