import torch.nn as nn

class Model(nn.Module):
    def __init__(self, channel=32):
        super().__init__()

        self._conv = nn.ConvXd(1084)
        self._batchnorm = nn.BatchNormXd()
        self._relu = nn.ReLU()

    def forward(self, input_tensor):
        
        conv = self._conv(input_tensor)
        conv = self._batchnorm(conv) 
        output  = conv
        return output
