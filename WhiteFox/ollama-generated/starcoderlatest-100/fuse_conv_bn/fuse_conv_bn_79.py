 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 10, kernel_size=3)

    def forward(self, x1):
        return self.conv(x1)


# Inputs to the model
x1 = torch.randn(4, 2, 4, 4)
