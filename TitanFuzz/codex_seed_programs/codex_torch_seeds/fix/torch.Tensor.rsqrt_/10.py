'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rsqrt_\ntorch.Tensor.rsqrt_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor:', input_tensor)
print('\nOutput Tensor:', input_tensor.rsqrt_())