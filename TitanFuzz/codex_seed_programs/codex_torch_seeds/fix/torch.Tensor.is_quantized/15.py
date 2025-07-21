'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_quantized\ntorch.Tensor.is_quantized(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(1, 1, 1, 1)
_output_tensor = torch.Tensor.is_quantized(_input_tensor)
print('The result is: ', _output_tensor)