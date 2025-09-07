
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.batch_norm(v1, running_mean=..., running_var=...)  # Tracking of statistics with running_mean and running_var variables.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)
