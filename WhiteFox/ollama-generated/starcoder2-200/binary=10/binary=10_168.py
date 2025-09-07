
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        if self._is_module and not isinstance(other, torch.Tensor):
            raise TypeError('Argument 2 (other) should be a tensor')
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
 
        # Check if the second conv is missing or not
        v3 = v2 if self._is_module else other
        v4 = torch.addmm(v3, 0., 1.)
        return v4


# Initializing the model