
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(**kwargs)
        self.bn = torch.nn.BatchNorm2d(num_features=16, eps=1e-5, momentum=0.1, affine=True)

    def forward(self, x):
        return self.bn(self.conv(x))

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(4, 2, 3, 5)
