'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(3, 4, 5)
_output_tensor = _input_tensor.char()
print(_output_tensor)