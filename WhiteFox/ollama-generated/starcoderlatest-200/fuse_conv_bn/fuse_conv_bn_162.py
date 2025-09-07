
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, (3,3))
        self.bn  = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        v1 = self.conv(x1).permute(0, 2, 3, 1) # The output is in NCHW format
        v2 = torch.nn.functional.batch_norm(v1, self.bn.weight, self.bn.bias,
                                          self.bn.running_mean, self.bn.running_var)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 5, 4)
