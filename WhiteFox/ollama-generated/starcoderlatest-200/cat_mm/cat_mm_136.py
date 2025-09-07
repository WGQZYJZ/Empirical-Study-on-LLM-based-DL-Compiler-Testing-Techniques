
class Model(torch.nn.Module):
    def __init__(self, n_input: int = 3, n_output: int = 8, stride: int = 1, padding: int = 1):
        super().__init__()
        self.conv = torch.nn.Conv2d(n_input, n_output, kernel_size=1, stride=stride, padding=padding)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + self.conv(x2)
        return torch.cat([v1, v2])


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
