
class Model(torch.nn.Module):
    def __init__(self, input_channels: int = 3):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_channels, 8, kernel_size=1, stride=1)
 
    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1 for _ in range(6)])
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
