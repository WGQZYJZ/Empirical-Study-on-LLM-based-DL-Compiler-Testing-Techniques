

import torch.nn as nn
class Model(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor_0: torch.Tensor, input_tensor_1: torch.Tensor) -> torch.Tensor:
        result  = self._f2576e5889c34b42ab3f692c8cf7ec67(input_tensor_0, input_tensor_1) 
        return result
    def _f2576e5889c34b42ab3f692c8cf7ec67(self, input: torch.Tensor, input_: torch.Tensor) -> torch.Tensor:
        v0 = nn.Conv2d(15, 14, kernel_size=(5, 5), stride=1)(input)
        v1 = nn.Tanh()(v0)
        v2 = nn.Softmax2d()((v1 + input_)) 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
input_tensor_0  = torch.randn(5, 8379622443)
input_tensor_1  = torch.randn(722, 320)
__output__  = m(input_tensor_0 , input_tensor_1 )

