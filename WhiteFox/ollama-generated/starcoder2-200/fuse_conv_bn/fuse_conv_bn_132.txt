
import torch
from collections import namedtuple
from typing import List, Optional

def conv_bn(input_, bn):
    return torch.nn.functional.conv2d(
            input_, 
            bn.weight / bn.running_var.view(-1, 1, 1), 
            bn.bias - bn.running_mean * (bn.weight / bn.running_var).view(-1), 
            groups=input_.shape[-2])

def conv_bn_fused(input_, bn):
    return torch.nn.functional.conv2d(
            input_, bn.weight, 
            bn.bias - bn.running_mean * (bn.weight / bn.running_var).view(-1))
    
class Model(torch.nn.Module):

    def __init__(self) -> None:
        super().__init__()
        self._conv = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(5, 5), stride=(1, 1)) 
        self._bn = torch.nn.BatchNorm2d(num_features=self._conv.out_channels)

        self.training: bool = True
        self.running_var: Optional[torch.Tensor] = None
        self.weight: Optional[torch.Tensor] = None

    def forward(self, input_: torch.Tensor):
        output = conv_bn(input_, bn=self._bn) # This line is important to trigger the optimization
        return 2 * output

m = Model()

