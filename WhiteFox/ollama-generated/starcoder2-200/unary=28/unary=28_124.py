
class Model(torch.nn.Module):
    def __init__(self, minv=2048., maxv=-16384.):
        super().__init__()
        self.linear  = torch.nn.Linear(768 * 512, 29)
        self._minval = minv
        self._maxval = maxv
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = torch.clamp_min(v1, self._minval) 
        v4 = torch.clamp_max(v3, self._maxval) 
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(50, 768 * 512).view(-1, 768*512)
__output__= m(x1)




