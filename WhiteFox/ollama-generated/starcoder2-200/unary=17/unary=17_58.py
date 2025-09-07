
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x):
        v0 = F.relu(x)
        return self.conv(v0)


m  = Model()


x  = torch.randn(1, 8, 64, 64)

__output__  = m(x)

import torch.nn as nn 

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self._v0=torch.zeros([2])
        self._v1=MyLayer(self._v0)

    def forward(self, x):

        self._v0[0]=x[0]
        v1 = self._v1(
            self._v0
        )
        return [v1]

class MyLayer(nn.Module):
    def __init__(self,_v0=None):
         super().__init__()
         self._v0=_v0
         self._v1=torch.zeros([2])

    @torch.no_grad()
    def forward(self,x):
        self._v0[1]=F.relu(x[0])

        v1 = self._v1 * 0.5
        return [v1]
