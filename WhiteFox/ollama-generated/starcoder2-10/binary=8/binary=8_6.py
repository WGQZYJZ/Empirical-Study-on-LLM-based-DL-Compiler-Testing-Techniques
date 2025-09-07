
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # convolution with kernel size 1
        v2 = v1 + self.__kwargs__["other"] # the addition is done to the output of the conv
        return v2


# Initializing the model
m = Model()
__output__  = m(**{"input": torch.randn(3, 8, 64, 64), "other" : torch.zeros((3, 8, 64, 64))})
