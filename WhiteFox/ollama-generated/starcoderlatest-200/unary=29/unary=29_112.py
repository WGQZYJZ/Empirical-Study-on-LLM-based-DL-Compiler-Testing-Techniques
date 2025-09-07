
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=4, padding=0, output_padding=0)
        self._min = min_value
        self._max = max_value
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min=self._min)
        v3 = torch.clamp_max(v2, max=self._max)
        return v3

 # Initializing the model
m = Model(0., 5.)
 
 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
