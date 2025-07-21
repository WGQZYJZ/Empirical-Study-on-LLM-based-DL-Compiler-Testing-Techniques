'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = _input_tensor.cuda()
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_output_tensor))