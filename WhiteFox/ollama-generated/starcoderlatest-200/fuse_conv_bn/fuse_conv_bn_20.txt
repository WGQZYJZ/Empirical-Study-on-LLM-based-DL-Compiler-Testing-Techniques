
class Model(torch.nn.Module):
    def __init__(self, conv, bn, act):
        super().__init__()
        self.conv = conv()
        self.bn = bn()
        self.act = act

    def forward(self, x):
        x  = self.conv(x)
        if not self.training:
            return torch.nn.functional.batch_norm(
                x, 
                None, 
                self.bn.running_mean,
                self.bn.running_var,
                True,
                self.act() if self.training else None
            )
        return self.act()(x)
# Initializing the model
m = Model(
    conv=lambda: torch.nn.Conv2d(2, 2, kernel_size=3),
    bn=lambda: torch.nn.BatchNorm2d(2),
    act=lambda: torch.nn.ReLU(),
)

# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
