'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
from torch.autograd import Variable
_input = torch.randn(2, 3, 4)
_input_tensor = Variable(_input)
_input_tensor_cuda = _input_tensor.cuda()
print(_input_tensor_cuda)