'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.bool()
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)