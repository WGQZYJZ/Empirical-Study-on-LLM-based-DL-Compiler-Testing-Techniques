'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_quantized\ntorch.Tensor.is_quantized(_input_tensor, )\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print('The result of calling torch.Tensor.is_quantized is: {}'.format(torch.Tensor.is_quantized(input_tensor)))