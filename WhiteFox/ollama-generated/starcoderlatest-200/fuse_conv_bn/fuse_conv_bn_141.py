
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, kernel_size=5)
        self.batch_norm = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        out = self.conv(x)
        # Batch norm should not be invoked if it is used by other nodes
        out = self.batch_norm(out)
        return out


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 1, 32, 32)
