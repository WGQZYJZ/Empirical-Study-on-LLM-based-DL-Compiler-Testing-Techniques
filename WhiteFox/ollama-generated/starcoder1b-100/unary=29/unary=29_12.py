
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value, max_value=None):
        v1 = self.conv(x1)
        if max_value:
            v2 = torch.clamp_max(v1, max_value) - 1 # -1 is needed because PyTorch returns the original output in a different order of channels * height * width
        else:
            v2 = torch.clamp_min(v1, min_value) + 1 # +1 is needed because PyTorch returns the original output in a different order of channels * height * width
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
min_value = -50 # Value for min_value keyword argument
