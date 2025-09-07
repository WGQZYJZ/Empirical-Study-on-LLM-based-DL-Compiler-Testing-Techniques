
class Model(torch.nn.Module):
    def __init__(self, conv_fn1, bn_fn1):
        super().__init__()

        self.conv = conv_fn1()  # Conv layer with input channels == output channels of the BN layer, not necessarily equal to 3.
        self.bn   = bn_fn1(conv=True)

    def forward(self, x0):
       v1 = self.conv(x0)

       if isinstance(v1, tuple):
            v2, _ = v1 # conv output is in the first tuple element
            v3    = torch.nn.functional.batch_norm(v2)
            return (v2,) + v3
        else:
            v2  = self.bn(v1, self.bn._module_name())
            return v2

# Initializing the model
m   = Model(lambda : torch.nn.Conv1d(64, 64, 7), lambda x=True: torch.nn.BatchNorm1d(3))
x0  = torch.randn(5, 64, 2)


__output__  = m(x0)
