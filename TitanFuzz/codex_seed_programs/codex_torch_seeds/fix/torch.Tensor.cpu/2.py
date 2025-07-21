'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(3, 3, requires_grad=True)
print('Input tensor is: ', _input_tensor)
_cpu_tensor = torch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)
print('CPU tensor is: ', _cpu_tensor)