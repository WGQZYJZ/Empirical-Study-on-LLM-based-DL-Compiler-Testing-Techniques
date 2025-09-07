
class Model(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(embed_dim, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1

# Initializing the model
m = Model(30)

# Inputs to the model
x1 = torch.randn(1, 30, 64, 64)
