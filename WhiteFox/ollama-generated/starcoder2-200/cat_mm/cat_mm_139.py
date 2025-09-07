class Model(torch.nn.Module):
    def __init__(self, inChannels=32, outChannels=64, ksize=1):
        super().__init__()
        
        self._conv = torch.nn.Conv2d(inChannels, outChannels, 
                                      kernel_size=ksize, stride=stride)
    
    def forward(self, x): 
        v1 = self._conv(x)
        return [v1] + v1 * 0.5 + v1
