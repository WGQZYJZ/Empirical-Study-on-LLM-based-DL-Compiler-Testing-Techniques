'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)
print(_output_tensor)