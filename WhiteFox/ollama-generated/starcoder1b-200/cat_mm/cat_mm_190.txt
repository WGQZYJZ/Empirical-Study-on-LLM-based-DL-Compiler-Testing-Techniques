
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        # Concatenate the outputs of the two input tensors along the third dimension
        return torch.cat([v1, v2], 3)


# Initializing the model
m = Model()
__input1__ = torch.randn(1, 3, 64, 64)
__input2__ = torch.randn(1, 3, 64, 64)
x = m(__input1__, __input2__)

