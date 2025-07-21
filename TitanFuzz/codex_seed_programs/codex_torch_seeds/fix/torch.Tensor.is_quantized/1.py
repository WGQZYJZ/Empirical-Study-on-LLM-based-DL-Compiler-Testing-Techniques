'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_quantized\ntorch.Tensor.is_quantized(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(2, 2)
_output = torch.Tensor.is_quantized(_input_tensor)
print('Output: ', _output)