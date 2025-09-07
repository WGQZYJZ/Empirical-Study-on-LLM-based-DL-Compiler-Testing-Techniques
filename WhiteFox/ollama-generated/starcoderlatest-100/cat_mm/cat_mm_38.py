
class Model(torch.nn.Module):
    def __init__(self, num_dims=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=num_dims)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1])
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
