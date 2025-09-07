
class Model(torch.nn.Module):
    def __init__(self, conv: torch.nn.ConvXd):
        super().__init__()
        self.conv = conv

    def forward(self, x):
        return self.conv(x)


# Initializing the model
m = Model(torch.nn.Conv2d(...))
