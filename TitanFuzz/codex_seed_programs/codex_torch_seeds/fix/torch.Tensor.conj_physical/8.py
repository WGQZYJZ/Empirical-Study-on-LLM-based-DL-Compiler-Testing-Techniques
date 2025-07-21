'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical\ntorch.Tensor.conj_physical(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
_input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.conj_physical(_input_tensor)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', output_tensor)