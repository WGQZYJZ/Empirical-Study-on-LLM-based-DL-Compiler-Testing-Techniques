'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:\n', input_tensor)
print('\nIs input tensor -inf?', input_tensor.isneginf())
input_tensor[0][0] = float('-inf')
print('\nIs input tensor -inf?', input_tensor.isneginf())
input_tensor[0][0] = float('inf')
print('\nIs input tensor -inf?', input_tensor.isneginf())