
class Model(torch.nn.Module):
    def __init__(self, input_dim=32, kernel_size=16):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim, 8, kernel_size, stride=1, padding=0)

    def forward(self, x1):
        return self.conv(x1)


# Inputs to the model
input_tensor = torch.randn((1, 3, 64, 64))
