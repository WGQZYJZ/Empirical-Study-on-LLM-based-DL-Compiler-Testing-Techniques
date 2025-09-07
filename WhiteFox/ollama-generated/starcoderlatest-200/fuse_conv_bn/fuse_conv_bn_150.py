
class Model(torch.nn.Module):
    def __init__(self, stride=1):
        super().__init__()
        self.stride = stride
        if stride != 1:
            kernel_size = 2
            padding = (kernel_size - 1) // 2
            self.conv = torch.nn.Conv2d(3, 3, kernel_size, padding=padding)

    def forward(self, x):
        x = self.conv(x)
        return x


# Inputs to the model
x1 = torch.randn(1, 3, 4, 5)
