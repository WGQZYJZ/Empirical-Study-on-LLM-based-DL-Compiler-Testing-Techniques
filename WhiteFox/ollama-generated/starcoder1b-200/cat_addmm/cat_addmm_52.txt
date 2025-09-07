
class Model(torch.nn.Module):
    def __init__(self, x1_shape=(3, 64, 64)):
        super().__init__()
        self.conv = torch.nn.Conv2d(x1_shape[0], 8, kernel_size=1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.cat([v1, v1], dim=-1)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(*x1_shape)
