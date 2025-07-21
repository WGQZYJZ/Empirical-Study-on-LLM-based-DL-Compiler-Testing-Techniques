'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
_input_tensor = torch.randn(3, 2, 2, 2)
print('Input tensor:\n{}'.format(_input_tensor))
_contiguous_tensor = _input_tensor.contiguous()
print('Contiguous tensor:\n{}'.format(_contiguous_tensor))