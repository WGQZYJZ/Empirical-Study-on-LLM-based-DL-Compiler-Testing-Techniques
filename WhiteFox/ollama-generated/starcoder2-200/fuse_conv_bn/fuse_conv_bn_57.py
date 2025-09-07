
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()

        self.conv  = torch.nn.Conv1d(3, 5, kernel_size=7)
        self.bn    = torch.nn.BatchNorm2d(5)

    def forward(self, x1):
        v1   = x1.permute((0, 2, 1))
        v2   = torch.nn.functional.conv3d(v1, conv_weights, self.conv.bias)

        return self.bn(v2)

# Inputs to the model
x1  = torch.randn(1, 3, 7, 5)
__output__  = m(x1)


