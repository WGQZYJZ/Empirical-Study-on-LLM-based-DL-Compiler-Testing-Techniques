'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_is_contiguous = torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)
print('Is contiguous: {}'.format(_is_contiguous))