
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=127):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 4)
        self._min_value = min_value
        self._max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self._min_value)
        v3 = torch.clamp_max(v2, self._max_value)
        return v3


# Initializing the model with a minimum value of -1 and a maximum value of 0
m = Model(-1, 0)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
