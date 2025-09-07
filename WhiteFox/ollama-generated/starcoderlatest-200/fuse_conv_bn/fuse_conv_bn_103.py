
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 2)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        output = self.bn(self.conv(x))
        return output


# Initializing the model and registering the optimization passes in the execution environment
m = Model()
set_fusion(m)
__input__ = torch.randn(1, 1, 8, 240, requires_grad=True)
print("Fusion pattern is ", m)


# Run the model
print(__output__)

