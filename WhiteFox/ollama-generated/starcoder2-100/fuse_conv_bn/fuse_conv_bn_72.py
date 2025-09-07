
class FuseConvBN(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.conv3d(x1, self.linear.weight, self.linear.bias)

        return v2


# Initializing the model