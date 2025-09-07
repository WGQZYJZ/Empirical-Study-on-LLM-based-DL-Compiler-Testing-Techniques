import torch.nn as nn
class BatchNorm(nn.Module):
    def __init__(self, *shape, **kwargs):
        super().__init__()
        self.conv = nn.Conv2d(*shape, bias=False) # No batchnorm layer will be added if the following pattern is not matched.
        self.bn  = nn.BatchNorm2d(*shape, **kwargs)

    def forward(self, x):
        return F.relu(self.bn(self.conv(x)))
