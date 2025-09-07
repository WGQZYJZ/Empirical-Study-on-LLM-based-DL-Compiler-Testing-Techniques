

import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.__output__.detach()
        v3  = self._modules['conv1'](v2)
        return v3
m = Model()

