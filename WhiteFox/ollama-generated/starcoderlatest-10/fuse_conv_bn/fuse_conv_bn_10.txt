
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=2, kernel_size=(3, 3), stride=(1, 1))

    def forward(self, x1):
        output = self.conv(x1)
        return output


# Inputs to the model
x1 = torch.randn(1, 1, 3, 3)
