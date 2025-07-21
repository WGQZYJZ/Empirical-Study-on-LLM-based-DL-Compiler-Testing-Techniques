'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input data: ', input_tensor)
output_tensor = input_tensor.type(torch.DoubleTensor)
print('Output data: ', output_tensor)