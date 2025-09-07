
class Model(torch.nn.Module):
    def __init__(self, n_in=10, n_out=8):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(n_in, 32, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(32, n_out, kernel_size=4)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1, v1], dim=1)
        return self.conv2(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 10, 64, 64)
