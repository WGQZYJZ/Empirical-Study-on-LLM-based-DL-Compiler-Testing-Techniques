
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, (3, 5))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.batch_norm(v1, True, True) # `track_running_stats` is set to be `True`.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
