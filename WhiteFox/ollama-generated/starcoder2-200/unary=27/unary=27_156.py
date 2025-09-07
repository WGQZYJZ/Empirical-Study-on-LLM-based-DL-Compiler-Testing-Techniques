
class Model(torch.nn.Module):
    def __init__(self, max_value=10.0, min_value=-25.73648297):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2   = torch.clamp_min(v1, min_value=self._min_value_) # Clamp the output of the convolution to a minimum value
        v3   = torch.clamp_max(v2, max_value=self._max_value_) # Clamp the output of the previous operation to a maximum value
        return v3


m  = Model()
m.__output__  = m(x1)


