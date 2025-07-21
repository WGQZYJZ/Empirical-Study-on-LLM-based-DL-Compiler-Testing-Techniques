'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
_output_tensor = torch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)
print('Output is ', _output_tensor)