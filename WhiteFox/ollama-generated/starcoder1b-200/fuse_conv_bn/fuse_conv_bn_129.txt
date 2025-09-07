
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def conv(self, x1):
        return torch.nn.functional.conv2d(...)

    def bn(self, x1):
        return torch.nn.functional.batch_norm2d(...)

    @torch.jit.script_method
    def forward(x1):
        v1 = self.conv(x1)
        return self.bn(v1)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 20, 20)
