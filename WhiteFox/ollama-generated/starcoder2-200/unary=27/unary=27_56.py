
class Model(torch.nn.Module):
    def __init__(self, max_value=5., min_value=-20.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min=self.min_value) # Clamp to the minimum value
        v3  = torch.clamp_max(v2, max=self.max_value) # Clamp to the maximum value

# Initializing the model with maximum and minimum values of -5 and +6.7 for example:
m1 = Model()

