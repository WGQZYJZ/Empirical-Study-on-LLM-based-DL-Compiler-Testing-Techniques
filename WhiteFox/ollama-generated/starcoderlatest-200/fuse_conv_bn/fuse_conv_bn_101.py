
class Model(torch.nn.Module):
    def __init__(self, dim=1, kernel_size=[3, 5]):
        super().__init__()
        self.conv = torch.nn.Conv2d(dim, dim, kernel_size)
        self.bn = torch.nn.BatchNorm2d(dim)

    def forward(self, x):
        # Only fusing batch norm layers with a single input if in training mode (e.g., training or inference).
        conv = self.conv if m.training else self.conv.eval()
        output = self.bn(conv(x))
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 5, 7)
