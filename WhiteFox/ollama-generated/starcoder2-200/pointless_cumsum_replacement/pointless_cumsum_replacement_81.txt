

import torch  # pylint: disable=wrong-import-position

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg0, arg1):
        t1 = torch.full([arg0], 4398046511104)
        t2 = self._convert_element_type(t1, torch.float32)
        t3 = self._cumsum(t2, dim=1) # pylint: disable=no-member
        return t3

    def _convert_element_type(self, v1):
        return v1  # pylint: disable=unused-argument
    
    def _cumsum(self, v0, dim):
        return v0


# Initializing the model
m = Model()
 
# Inputs to the model
arg0  = torch.randn([2])
arg1  = torch.randn([4398046511104, 2], dtype=torch.float32) # pylint: disable=unexpected-keyword-arg
__output__  = m(arg0, arg1)

