
class Model(torch.nn.Module):
    def __init__(self, n_in: int = 3, n_out: int = 8):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(n_in, n_out, kernel_size=1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(n_out, n_out, kernel_size=3, stride=1, padding=1)
 
    def forward(self, x: torch.Tensor):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
 
        return torch.cat([v2], dim=1)


# Initializing the model and inputs to the model
m = Model()
x = torch.randn(1, 3, 64, 64)
