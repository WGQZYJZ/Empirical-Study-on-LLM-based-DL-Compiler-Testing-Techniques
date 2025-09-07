class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.Conv2d(in_channels=3, out_channels=4, kernel_size=(10))
        bn  = torch.nn.BatchNorm2d(num_features=conv.out_channels)
        return bn(conv(x1))


m = Model()


x1  = torch.randn(1, 3, 8, 4)
__output__  = m(x1)
import torch
class ConvBlock(torch.nn.Module):
    def __init__(self, in_channel, out_channels, kernel=20, stride=None):
        super().__init__()
        
        if stride is None:
            self._stride  = (1,) * len(kernel)

        else: 
            self._stride  = stride
    
        self._conv  = torch.nn.ConvXd(in_channel, out_channels[0], kernel)
        
    def forward(self, x):
        return self._conv(x).relu(inplace=True)
    
    @property
    def stride(self):
         return self._stride
