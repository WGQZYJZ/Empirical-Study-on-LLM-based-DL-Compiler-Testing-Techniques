
class Module(torch._jit_internal.FusedModule):
    def __init__(self):
        super().__init__()
        self.linear  = torch._jit_internal.Conv2dNd(...)
        self.bn     = torch._jit_internal.BatchNorm2dNd(...)

    @torch.jit.export()
    def forward(self, x1):
        v1 = self.conv(x1)
        return self.bn(v1)


# Initializing the model
m  = Module()

 # Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
