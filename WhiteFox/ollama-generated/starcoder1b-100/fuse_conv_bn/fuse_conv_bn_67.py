
class Module(torch.nn.Module):
    def __init__(self, conv):
        super().__init__()
        self.conv = conv

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return torch.nn.functional.convXd(v1, self.conv.weight, self.conv.bias)

m = Module(torch.nn.ConvNd(1, 2, (2, 2)))

# Inputs to the model
x1 = torch.randn(1, 2, 2)
