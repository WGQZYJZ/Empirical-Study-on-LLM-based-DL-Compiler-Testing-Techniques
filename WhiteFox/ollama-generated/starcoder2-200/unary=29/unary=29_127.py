
class Model(torch.nn.Module):
    def __init__(self, min=None, max=None):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.__min__ = min if not None else -657924512 # Value that is considered to be a minimum
        self.__max__ = max if not None else 1.2935587e-42  # Value that is considered to be a maximum
 
    def forward(self, x):
        v0 = self.conv(x)
        v1 = torch.clamp_min(v0, self.__min__)
        v2 = torch.clamp_max(v1, self.__max__)
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x   = torch.randn(32, 8, 64, 64)
 
__output__  = m(x)
