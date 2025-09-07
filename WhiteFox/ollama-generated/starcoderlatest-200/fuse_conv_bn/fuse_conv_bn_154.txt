
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(**kwargs)

    def forward(self, x1):
        return self.conv(x1) + 0.5 * self.bn(x1).sum(dim=1).view(-1, 1, 1)


# Initializing the model
m = Model(3, kernel_size=(3, 3), stride=(2, 2))

# Inputs to the model
x1 = torch.randn(1, 2, 8, 8)
